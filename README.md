# Bank Customer Churn Analysis

Analysis of customer churn patterns in banking using SQL and Python to identify factors that drive customer retention.

## Quick Start

**Just want to see the analysis?** Click on [`Bank_Churn_Analysis.ipynb`](Bank_Churn_Analysis.ipynb) to view the full notebook with all visualizations and code.

**Want to run it yourself?** See the [setup instructions](#setup) below.

## About This Project

I built this project to demonstrate SQL and Python data analysis skills, focusing on a real business problem in banking. Customer churn is expensive - it costs 5-7x more to acquire new customers than retain existing ones - so understanding what drives customers to leave is valuable.

The analysis uses a synthetic dataset of 10,000 bank customers and combines SQL queries with Python analysis to uncover patterns in churn behavior.

## Tech Stack

- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **SQL** (SQLite)
- **Jupyter Notebook**

## Dataset

Using the [Bank Customer Churn dataset from Kaggle](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn), which includes customer demographics, account details, product usage, and whether they churned.

## Analysis Approach

The notebook walks through:

1. SQL queries to extract and aggregate customer data
2. Data cleaning and validation in Python
3. Statistical analysis to identify churn patterns
4. Visualizations showing key findings
5. Business recommendations based on the data

I focused on making the insights actionable - not just "churn is bad" but specifically where it's happening and what might help.

## What I Found

A few interesting patterns emerged:

### Geography matters
Germany has 2x the churn rate of France or Spain (32% vs 16%)

![Churn by Geography](images/churn_by_geography.png)

This could indicate stronger banking competition in Germany, different customer expectations, or regional service quality differences.

---

### Activity is key
Inactive members churn at nearly double the rate of active ones (27% vs 14%)

![Active vs Inactive Members](images/churn_by_activity.png)

Makes sense. If you're not using your account, you woould be more likely to leave.

---

### Complaints are basically an exit signal
Customers who complained show near 100% churn

![Complaint Impact on Churn](images/churn_by_complaint.png)

This is the most dramatic finding. Complaints aren't just frustrations - they're the last step before customers leave. How complaints are handled (or not handled) clearly makes or breaks retention.

---

### Age patterns
Middle-aged customers (40-60) churn significantly more than younger or older segments

![Churn by Age Group](images/churn_by_age_group.png)

This demographic likely has more complex financial needs - mortgages, kids' college funds, retirement planning. They're probably looking around more for better offers or services.

---

### The product problem
Here's where it gets weird: customers with 3-4 products churn MORE, not less

![Churn by Number of Products](images/churn_by_num_of_prod.png)

In real banking, having multiple products usually increases loyalty - you're more embedded in the ecosystem. The fact that this shows the opposite suggests one of two things:

1. **It's synthetic data** (which it is - from Kaggle) that doesn't reflect actual customer behavior
2. **If this were real**, it would point to a serious product quality or service issue - maybe forced cross-selling, products that don't fit customer needs, or poor service for multi-product customers

This finding is a good reminder that you can't just trust the data. You need to question patterns that contradict domain knowledge and investigate before making strategic changes.

## Business Impact

Reducing churn has direct financial implications:

**Current State:**
- 10,000 customers analyzed
- 20.4% churn rate (2,038 customers lost)
- Average customer balance: $76,485

**Projected Impact:**
If churn is reduced by just 5 percentage points (20.4% → 15.4%):
- **~500 additional customers retained annually**
- **~$38M in customer balances preserved**
- Significant reduction in acquisition costs (new customers cost 5-7x more than retention)

**Fix Germany first** - 32% churn vs 16% elsewhere is a red flag. Need targeted campaigns there, maybe even investigate if there's a service quality issue.

**Go after inactive members** - They're churning at double the rate. Set up automated re-engagement - special offers, check-in calls, whatever gets them using their accounts again.

**Treat complaints like emergencies** - Near 100% churn after complaints means the resolution process is broken. Fast-track these, follow up after, and measure satisfaction.

**Rethink the 40-60 demographic** - They're leaving because their needs aren't being met. This age group needs financial planning, college savings, retirement advice - not just basic checking accounts.

**Investigate the product thing** - If this were real data showing more products = more churn, I'd be asking: Are we forcing products people don't want? Is service quality dropping for multi-product customers? Are we making banking more complicated instead of easier?

---

**Note on Data:** This analysis uses a synthetic Kaggle dataset for demonstration purposes. The product usage finding (more products = more churn) contradicts real-world banking research, which typically shows the opposite. This highlights the importance of validating findings against domain knowledge and actual business data before making strategic decisions.

## Project Structure

```
bank-customer-churn-analysis/
├── data/
│   ├── Customer-Churn-Records.csv
│   └── bank_churn.db
├── Bank_Churn_Analysis.ipynb
├── load_data.py
├── requirements.txt
└── README.md
```

## Setup

If you want to run the notebook locally:

1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/bank-customer-churn-analysis.git
cd bank-customer-churn-analysis
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Load the data into SQLite
```bash
python load_data.py
```

4. Open the notebook
```bash
jupyter notebook Bank_Churn_Analysis.ipynb
```

## Requirements

- Python 3.8+
- pandas, numpy, matplotlib, seaborn, jupyter
- sqlite3 (comes with Python)

## What's Next

Some ideas for extending this project:
- Build a predictive model to identify at-risk customers before they churn
- Add time-series analysis to see how churn patterns change over time
- Test retention strategies with A/B testing framework

## About Me

I'm Jamyang Ponsar, a recent Computer Science grad from Stony Brook University interested in data science and analytics.

[LinkedIn](https://linkedin.com/in/jamyangponsar) | [GitHub](https://github.com/JamPonsar)
