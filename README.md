# Bank Customer Churn Analysis

## Project Overview
Analysis of customer churn patterns in banking to identify at-risk customers and provide actionable retention strategies for financial institutions.

## Technologies Used
- **Python**: Pandas, NumPy, Matplotlib, Seaborn
- **SQL**: SQLite for data storage and querying
- **Jupyter Notebook**: Interactive analysis and visualization

## Dataset
Source: [Bank Customer Churn Dataset on Kaggle](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn)

The dataset contains customer information including:
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
│   ├── bank_churn.csv          # Raw dataset
│   └── bank_churn.db           # SQLite database
│
├── Bank_Churn_Analysis.ipynb   # Main Jupyter notebook
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
└── .gitignore                   # Git ignore file
```

## Key Findings
- Geography has significant impact on churn rates
- Inactive members show substantially higher churn
- Customer age and number of products correlate with churn behavior
- Account balance patterns differ between retained and churned customers

## Analysis Highlights
- **SQL Queries**: Extraction and aggregation of customer data
- **Data Cleaning**: Handling missing values and data validation
- **Exploratory Analysis**: Statistical analysis of churn patterns
- **Visualizations**: Charts showing churn by demographics, geography, and account characteristics
- **Business Insights**: Actionable recommendations for customer retention

## How to Run

### Prerequisites
```bash
pip install -r requirements.txt
```

### Steps
1. Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/bank-customer-churn-analysis.git
cd bank-customer-churn-analysis
```

2. Install dependencies
```bash
pip install pandas numpy matplotlib seaborn jupyter sqlite3
```

3. Open Jupyter Notebook
```bash
jupyter notebook Bank_Churn_Analysis.ipynb
```

4. Run all cells to see the analysis

## Requirements
- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- jupyter
- sqlite3 (included in Python standard library)

## Author
Jamyang Ponsar

## License
This project is open source and available under the MIT License.
