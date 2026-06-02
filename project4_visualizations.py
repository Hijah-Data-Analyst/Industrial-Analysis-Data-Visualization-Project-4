"""
Project 4: Data Visualization - Industrial Analysis
Tool: Python (pandas + matplotlib)
Answers all 6 objectives from the business requirements
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np
from openpyxl import load_workbook

# ─────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────
wb = load_workbook('/mnt/user-data/uploads/Dataset_for_Data_Analytics.xlsx')
ws = wb.active
data = list(ws.values)
headers = data[0]
df = pd.DataFrame(data[1:], columns=headers)

# Fix types
df['Date'] = pd.to_datetime(df['Date'])
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
df['TotalPrice'] = pd.to_numeric(df['TotalPrice'], errors='coerce')
df['ItemsInCart'] = pd.to_numeric(df['ItemsInCart'], errors='coerce')

# ─────────────────────────────────────────────
# KPI CALCULATIONS
# ─────────────────────────────────────────────
total_quantity   = df['Quantity'].sum()
avg_unit_price   = df['UnitPrice'].mean()
avg_total_price  = df['TotalPrice'].mean()
items_in_cart    = df['ItemsInCart'].sum()

print("=" * 50)
print("KPI SUMMARY")
print("=" * 50)
print(f"Total Quantity   : {total_quantity:,.0f}")
print(f"Avg Unit Price   : ${avg_unit_price:,.2f}")
print(f"Avg Total Price  : ${avg_total_price:,.2f}")
print(f"Items in Cart    : {items_in_cart:,.0f}")
print()

# ─────────────────────────────────────────────
# CHART STYLE HELPER
# ─────────────────────────────────────────────
BLUE     = '#2563EB'
DARK     = '#1E293B'
GREY     = '#64748B'
LIGHT_BG = '#F8FAFC'
ACCENT   = '#0EA5E9'

def style_axis(ax):
    ax.set_facecolor(LIGHT_BG)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CBD5E1')
    ax.spines['bottom'].set_color('#CBD5E1')
    ax.tick_params(colors=GREY, labelsize=9)
    ax.yaxis.label.set_color(GREY)
    ax.xaxis.label.set_color(GREY)

# ─────────────────────────────────────────────
# CHART 1 – Total Quantity by Order Status (Clustered Bar)
# Objective: Which Order Status has the highest quantity?
# ─────────────────────────────────────────────
qty_status = df.groupby('OrderStatus')['Quantity'].sum().sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(9, 5))
fig.patch.set_facecolor('white')
colors = [BLUE if v == qty_status.max() else '#93C5FD' for v in qty_status.values]
bars = ax.barh(qty_status.index, qty_status.values, color=colors, edgecolor='white', linewidth=0.6)
for bar in bars:
    ax.text(bar.get_width() + 30, bar.get_y() + bar.get_height()/2,
            f'{bar.get_width():,.0f}', va='center', ha='left', fontsize=9, color=DARK)
ax.set_title('Shipped Orders Dominate: Highest Quantity by Order Status',
             fontsize=12, fontweight='bold', color=DARK, pad=12)
ax.set_xlabel('Total Quantity', fontsize=10)
ax.set_ylabel('Order Status', fontsize=10)
style_axis(ax)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/chart1_quantity_by_order_status.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Chart 1 saved: Total Quantity by Order Status")

# ─────────────────────────────────────────────
# CHART 2 – Total Quantity Over Time (Line Chart)
# Objective: Trends in order quantity over time
# ─────────────────────────────────────────────
df['YearMonth'] = df['Date'].dt.to_period('M')
qty_time = df.groupby('YearMonth')['Quantity'].sum().reset_index()
qty_time['YearMonth_str'] = qty_time['YearMonth'].astype(str)

fig, ax = plt.subplots(figsize=(12, 5))
fig.patch.set_facecolor('white')
ax.fill_between(range(len(qty_time)), qty_time['Quantity'], alpha=0.12, color=BLUE)
ax.plot(range(len(qty_time)), qty_time['Quantity'], color=BLUE, linewidth=2, marker='o', markersize=4)

# Only show every 6th label to avoid crowding
step = max(1, len(qty_time)//12)
ax.set_xticks(range(0, len(qty_time), step))
ax.set_xticklabels(qty_time['YearMonth_str'][::step], rotation=45, ha='right', fontsize=8)
ax.set_title('Order Quantity Fluctuates Over Time — Seasonal Patterns Visible',
             fontsize=12, fontweight='bold', color=DARK, pad=12)
ax.set_xlabel('Month', fontsize=10)
ax.set_ylabel('Total Quantity', fontsize=10)
style_axis(ax)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/chart2_quantity_over_time.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Chart 2 saved: Total Quantity Over Time")

# ─────────────────────────────────────────────
# CHART 3 – Total Quantity by Coupon Code (Donut Chart)
# Objective: How does quantity vary across coupon codes?
# ─────────────────────────────────────────────
qty_coupon = df.groupby('CouponCode')['Quantity'].sum().sort_values(ascending=False)
palette = [BLUE, ACCENT, '#6EE7F7', '#BAE6FD', '#E0F2FE'][:len(qty_coupon)]

fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor('white')
wedges, texts, autotexts = ax.pie(
    qty_coupon.values,
    labels=qty_coupon.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=palette,
    pctdistance=0.78,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2.5}
)
for t in texts:    t.set_fontsize(10); t.set_color(DARK)
for a in autotexts: a.set_fontsize(9);  a.set_color('white'); a.set_fontweight('bold')
# Draw center hole for donut
circle = plt.Circle((0, 0), 0.55, color='white')
ax.add_patch(circle)
ax.text(0, 0, f'{qty_coupon.sum():,.0f}\nTotal', ha='center', va='center',
        fontsize=11, fontweight='bold', color=DARK)
ax.set_title('SAVE10 Coupon Drives the Most Orders by Quantity',
             fontsize=12, fontweight='bold', color=DARK, pad=14)
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/chart3_quantity_by_coupon_code.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Chart 3 saved: Total Quantity by Coupon Code")

# ─────────────────────────────────────────────
# CHART 4 – Average Total Price by Referral Source (Bar Chart)
# Objective: How does average total price differ by referral source?
# ─────────────────────────────────────────────
avg_price_ref = df.groupby('ReferralSource')['TotalPrice'].mean().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
fig.patch.set_facecolor('white')
colors = [BLUE if i == 0 else '#93C5FD' for i in range(len(avg_price_ref))]
bars = ax.bar(avg_price_ref.index, avg_price_ref.values, color=colors, edgecolor='white', linewidth=0.6, width=0.6)
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
            f'${bar.get_height():,.0f}', ha='center', va='bottom', fontsize=9, color=DARK)
ax.set_title('Direct Traffic Generates the Highest Average Order Value',
             fontsize=12, fontweight='bold', color=DARK, pad=12)
ax.set_xlabel('Referral Source', fontsize=10)
ax.set_ylabel('Average Total Price ($)', fontsize=10)
style_axis(ax)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/chart4_avg_price_by_referral_source.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Chart 4 saved: Avg Total Price by Referral Source")

# ─────────────────────────────────────────────
# CHART 5 – Items in Cart by Customer ID (Bar Chart - Top 15)
# Objective: Which customers have the highest items in cart?
# ─────────────────────────────────────────────
cart_cust = df.groupby('CustomerID')['ItemsInCart'].sum().sort_values(ascending=False).head(15)

fig, ax = plt.subplots(figsize=(11, 5))
fig.patch.set_facecolor('white')
colors = [BLUE if i < 3 else '#93C5FD' for i in range(len(cart_cust))]
bars = ax.bar(cart_cust.index, cart_cust.values, color=colors, edgecolor='white', linewidth=0.6, width=0.7)
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=8, color=DARK)
ax.set_title('Top 15 Customers with Highest Total Items in Cart',
             fontsize=12, fontweight='bold', color=DARK, pad=12)
ax.set_xlabel('Customer ID', fontsize=10)
ax.set_ylabel('Total Items in Cart', fontsize=10)
ax.tick_params(axis='x', rotation=45)
style_axis(ax)
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/chart5_items_in_cart_by_customer.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Chart 5 saved: Items in Cart by Customer ID")

# ─────────────────────────────────────────────
# CHART 6 – All Metrics by Product (Clustered Bar)
# Objective: How do KPIs vary across product?
# ─────────────────────────────────────────────
metrics_product = df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Avg_Unit_Price=('UnitPrice', 'mean'),
    Avg_Total_Price=('TotalPrice', 'mean'),
    Items_in_Cart=('ItemsInCart', 'sum')
).reset_index()

products = metrics_product['Product'].tolist()
x = np.arange(len(products))
width = 0.2

fig, ax = plt.subplots(figsize=(13, 6))
fig.patch.set_facecolor('white')

b1 = ax.bar(x - 1.5*width, metrics_product['Total_Quantity'],    width, label='Total Quantity',    color='#2563EB', edgecolor='white')
b2 = ax.bar(x - 0.5*width, metrics_product['Avg_Unit_Price'],    width, label='Avg Unit Price ($)', color='#0EA5E9', edgecolor='white')
b3 = ax.bar(x + 0.5*width, metrics_product['Avg_Total_Price'],   width, label='Avg Total Price ($)', color='#38BDF8', edgecolor='white')
b4 = ax.bar(x + 1.5*width, metrics_product['Items_in_Cart'],     width, label='Items in Cart',     color='#BAE6FD', edgecolor='white')

ax.set_title('Monitor & Phone Lead Across KPIs: All Metrics by Product',
             fontsize=12, fontweight='bold', color=DARK, pad=12)
ax.set_xlabel('Product', fontsize=10)
ax.set_ylabel('Value', fontsize=10)
ax.set_xticks(x)
ax.set_xticklabels(products, fontsize=10)
ax.legend(fontsize=9, framealpha=0.6)
style_axis(ax)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/chart6_all_metrics_by_product.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Chart 6 saved: All Metrics by Product")

print()
print("=" * 50)
print("ALL 6 CHARTS GENERATED SUCCESSFULLY!")
print("=" * 50)
