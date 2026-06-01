# Industrial Analysis Data Visualization Project 4
Data visualization project analyzing industrial business performance using Python (pandas &amp; matplotlib). Covers order trends, customer behavior, coupon usage, and product KPIs through 6 professional charts.

---

## Project Overview
The goal is to move beyond data exploration and deliver clear, executive-ready visualizations that communicate business insights through storytelling.

The project follows the three disciplines of a professional data analyst:
- **The Architect** — Choose the right chart for the right question
- **The Editor** — Remove clutter, maximize data clarity
- **The Storyteller** — Frame every chart around a business decision

## Business Objectives

The following 6 business questions were answered through data visualization:

| # | Objective | Chart Type |
|---|---|---|
| 1 | Which Order Status contains the highest quantity of items? | Horizontal Bar Chart |
| 2 | What are the trends in order quantity over time? | Line Chart |
| 3 | How does order quantity vary across different coupon codes? | Donut Chart |
| 4 | How does average total price differ by referral source? | Bar Chart |
| 5 | Which customers have the highest total number of items in their carts? | Bar Chart |
| 6 | How do Key Performance Indicators (KPIs) vary across products? | Clustered Bar Chart |

---

## KPI Summary

| KPI | Value |
|---|---|
| Total Quantity | 3,535 |
| Average Unit Price | $356.41 |
| Average Total Price | $1,053.97 |
| Total Items in Cart | 6,582 |

---

## Key Insights

- **Shipped** orders account for the highest quantity of items among all order statuses
- Order quantity shows **seasonal fluctuations** across 2023–2024
- The **SAVE10 coupon** drives the most orders by quantity
- **Direct traffic** generates the highest average order value among all referral sources
- **Monitor and Phone** products lead across all KPIs

---

## Tools & Libraries

- **Language:** Python 3
- **Environment:** Jupyter Notebook
- **Libraries:**
  - `pandas` — data loading and aggregation
  - `matplotlib` — chart generation
  - `openpyxl` — reading Excel dataset
  - `numpy` — numerical operations

---

## File Structure

```
project4-data-visualization/
│
├── project4_visualizations.py          # Main Python script
├── Dataset_for_Data_Analytics.xlsx     # Source dataset (1,200 rows)
│
├── charts/
│   ├── chart1_quantity_by_order_status.png
│   ├── chart2_quantity_over_time.png
│   ├── chart3_quantity_by_coupon_code.png
│   ├── chart4_average_price_by_referral_source.png
│   ├── chart5_items_in_cart_by_customer.png
│   └── chart6_all_metrics_by_product.png
│
└── README.md
```

---

## How to Run

1. Clone this repository or download the files
2. Place `Dataset_for_Data_Analytics.xlsx` in the same folder as the script
3. Install the required libraries:

```bash
pip install pandas matplotlib openpyxl numpy
```

4. Open Jupyter Notebook and run:

```python
%matplotlib inline
%run project4_visualizations.py
```

Or open the `.py` file directly and run it in any Python environment.

---

## Chart Previews

### Chart 1 — Total Quantity by Order Status
![Chart 1](charts/chart1_quantity_by_order_status.png)

### Chart 2 — Total Quantity Over Time
![Chart 2](charts/chart2_quantity_over_time.png)

### Chart 3 — Total Quantity by Coupon Code
![Chart 3](charts/chart3_quantity_by_coupon_code.png)

### Chart 4 — Average Total Price by Referral Source
![Chart 4](charts/chart4_avg_price_by_referral_source.png)

### Chart 5 — Items in Cart by Customer ID
![Chart 5](charts/chart5_items_in_cart_by_customer.png)

### Chart 6 — All Metrics by Product
![Chart 6](charts/chart6_all_metrics_by_product.png)

---

## Conclusion
This project analyzed 1,200 rows of industrial business data and revealed that Shipped orders hold the highest item quantity, with seasonal fluctuations in demand across 2023–2024. The SAVE10 coupon drives the most orders, while Direct traffic generates the highest average order value. Monitor and Phone products consistently lead across all KPIs, with a total of 3,535 items ordered at an average price of $356.41.

---
