# Bank Customer Churn Analysis

## Project Overview
Analysis of customer churn patterns in banking to identify at-risk customers and provide actionable retention strategies for financial institutions.

**Why This Project?**
Customer churn costs banks millions in lost revenue. This analysis identifies key factors driving churn and provides data-driven recommendations to improve retention, directly relevant to financial services clients.

## 🔍 View the Analysis

**Option 1: View on GitHub (No Setup Required)**
Simply click on [`Bank_Churn_Analysis.ipynb`](Bank_Churn_Analysis.ipynb) in this repository to see the full analysis with all code, visualizations, and insights rendered directly on GitHub.

**Option 2: Run Locally**
Follow the [How to Run](#how-to-run) section below to execute the notebook on your own machine.

## Technologies Used
- **Python**: Pandas, NumPy, Matplotlib, Seaborn
- **SQL**: SQLite for data storage and querying  
- **Jupyter Notebook**: Interactive analysis and visualization

## Dataset
**Source**: [Bank Customer Churn Dataset on Kaggle](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn)

The dataset contains **10,000 customer records** with:
- Demographics (age, gender, geography)
- Account details (balance, tenure, credit score)
- Product usage (number of products, credit card holder status)
- Activity status (active member or not)
- Churn status (whether customer left the bank)

## Project Structure
```
bank-customer-churn-analysis/
│
├── data/
│   ├── Customer-Churn-Records.csv    # Raw dataset from Kaggle
│   └── bank_churn.db                 # SQLite database
│
├── Bank_Churn_Analysis.ipynb         # Main analysis notebook
├── load_data.py                      # Script to load CSV into SQLite
├── DEMO_SCRIPT.md                    # Presentation guide
├── README.md                         # Project documentation
├── requirements.txt                  # Python dependencies
└── .gitignore                        # Git ignore file
```

## Key Findings

📊 **Geographic Insights**
- Germany shows significantly higher churn rate (32.4%) compared to France (16.2%) and Spain (16.7%)
- Geographic targeting needed for retention campaigns

👥 **Customer Activity**
- Inactive members churn at 26.9% vs 14.3% for active members
- Engagement programs are critical for retention

⚠️ **Complaint Impact**  
- Customers with complaints show dramatically higher churn rates
- Customer service quality directly impacts retention

📈 **Age Demographics**
- Middle-aged customers (40-60) show higher churn rates
- Age-specific retention strategies recommended

💳 **Product Usage**
- Unexpected finding: customers with 3-4 products show higher churn
- May indicate product overload or poor cross-selling experience

## Analysis Highlights

### SQL Queries
- Overall churn statistics and baseline metrics
- Churn rate by geography, credit score, and demographics
- Active vs inactive member comparison
- Product usage and complaint analysis

### Python Data Analysis
- Data cleaning and validation
- Feature engineering (age groups, balance categories)
- Statistical analysis of churn patterns
- Correlation analysis across variables

### Data Visualizations
- 8 professional charts showing churn patterns
- Geographic comparison bar charts
- Distribution histograms
- Correlation heatmap
- Trend analysis by demographics

### Business Recommendations
- Immediate actions for high-risk segments
- Medium-term engagement strategies
- Long-term predictive modeling roadmap
- Quantified financial impact estimates

## How to Run

### Prerequisites
```bash
pip install -r requirements.txt
```

### Steps

1. **Clone this repository**
```bash
git clone https://github.com/JamPonsar/bank-customer-churn-analysis.git
cd bank-customer-churn-analysis
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Load data into SQLite database**
```bash
python load_data.py
```

4. **Open Jupyter Notebook**
```bash
jupyter notebook Bank_Churn_Analysis.ipynb
```

5. **Run all cells** to see the complete analysis

### Requirements
- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- jupyter
- sqlite3 (included in Python standard library)

## Project Highlights

✨ **What Makes This Project Special:**
- **Real-world relevance**: Directly applicable to financial services industry
- **End-to-end analysis**: From database queries to business recommendations
- **Professional visualizations**: Publication-ready charts and insights
- **Actionable insights**: Not just analysis, but concrete recommendations
- **Clean code**: Well-documented, modular, reproducible

## Key Insights Summary

**Current State:**
- 10,000 customers analyzed
- 20.38% overall churn rate
- 2,038 customers churned

**Potential Impact:**
If churn is reduced by just 5 percentage points:
- ~500 additional customers retained
- Approximately $38M in customer balances saved
- Significant improvement in customer lifetime value

## Next Steps

Future enhancements could include:
- Predictive churn model using machine learning
- Time-series analysis of churn trends
- Customer segmentation clustering
- A/B testing framework for retention campaigns
- Integration with external economic indicators

## Author
**Jamyang Ponsar**  
Recent Computer Science Graduate | Stony Brook University  
[LinkedIn](https://linkedin.com/in/jamyangponsar) | [GitHub](https://github.com/JamPonsar)

## License
This project is open source and available under the MIT License.

---

## 📝 Notes

**For Recruiters/Reviewers:**
This project demonstrates:
- SQL proficiency (complex queries, aggregations, joins)
- Python data analysis (Pandas, NumPy)
- Data visualization (Matplotlib, Seaborn)
- Business acumen (translating technical findings to actionable insights)
- Communication skills (clear documentation and presentation)

See [`DEMO_SCRIPT.md`](DEMO_SCRIPT.md) for the presentation walkthrough.
