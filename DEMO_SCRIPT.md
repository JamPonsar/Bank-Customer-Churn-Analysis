# Bank Churn Analysis - Demo Presentation Script

## TOTAL TIME: 15-20 MINUTES

---

## INTRODUCTION (2 minutes)

"Hi, thank you for this opportunity. Today I'm presenting a customer churn analysis project I built for the banking industry.

**Problem Statement:**
Customer churn is a critical issue for banks - losing customers means losing revenue, and it costs significantly more to acquire new customers than to retain existing ones. This analysis identifies the key factors driving churn and provides actionable recommendations for retention strategies.

**Project Overview:**
- Analyzed 10,000 customer records
- Used SQL for data extraction and aggregation
- Python (Pandas, NumPy) for data cleaning and analysis
- Created visualizations to communicate insights
- Delivered business recommendations based on findings

Let me walk you through the analysis."

---

## PART 1: SQL QUERIES (5-7 minutes)

### Section 2: Database Connection
"First, I'll connect to the SQLite database where I've stored the customer data."

[Run cell - show connection successful]

### Section 3.1: Overall Statistics
"Let's start with the big picture. I'll query the database to get our overall churn statistics."

[Run SQL query]

"As you can see, we have 10,000 customers with a churn rate of about 20%. This means roughly 1 in 5 customers have left the bank."

### Section 3.2: Geography Analysis
"Now let's break this down by geography to see if location impacts churn."

[Run SQL query]

"Interesting - we can see significant variation across countries. [Point to highest churn rate] has notably higher churn than the others."

### Section 3.4: Active vs Inactive
"One hypothesis is that customer activity level affects retention. Let me query that."

[Run SQL query]

"This is revealing - inactive members churn at a much higher rate. This suggests engagement is key to retention."

### ** LIVE MODIFICATION **
"Let me demonstrate my SQL skills by modifying this query. What if we wanted to see only customers from [specific country]?"

[Modify the query by adding WHERE clause]:
```sql
WHERE Geography = 'Germany'  -- or whatever country has highest churn
```

"There - now we're seeing only German customers, which helps us focus our retention efforts."

### Section 3.6: Complaints
"Finally, let's look at the impact of customer complaints."

[Run query]

"Wow - customers who have complained churn at a dramatically higher rate. This highlights the importance of complaint resolution."

---

## PART 2: PYTHON ANALYSIS (8-10 minutes)

### Section 4: Load Data
"Now I'll load the complete dataset into Python for deeper analysis."

[Run cell]

"Great - we have all 10,000 records with 18 features to analyze."

### Section 5: Data Cleaning
"Before analysis, we need to clean the data. Let me check for issues."

[Run cell]

"Good news - no missing values, no duplicates. I've also created some additional features like age groups and balance categories to help with segmentation."

### Section 6.1: Basic Statistics
"Let me calculate some key metrics."

[Run cell]

"These metrics give us a baseline understanding - average age is around 39, average balance is about $76K, and we have a 20% churn rate to work with."

### Section 6.2: Demographics
"Let's analyze churn by demographics."

[Run cell]

"Notice how churn varies significantly by age group - [point out highest]. This tells us we need age-specific retention strategies."

### ** LIVE MODIFICATION **
"Let me add a new analysis on the fly. What if I wanted to see churn rate for customers with balance over $100,000?"

[Add new cell and type]:
```python
high_balance_customers = df[df['Balance'] > 100000]
high_balance_churn = high_balance_customers['Exited'].mean() * 100
print(f"Churn rate for customers with >$100K balance: {high_balance_churn:.2f}%")
print(f"Number of such customers: {len(high_balance_customers)}")
```

[Run it]

"Interesting - [interpret the result]. This could inform our VIP customer retention program."

---

## PART 3: VISUALIZATIONS (5 minutes)

### Section 7.1: Geography
"Now let's visualize these patterns. First, churn by geography."

[Run cell - show chart]

"This bar chart clearly shows [highest churn country] as our problem area. Visual representation makes it easier for stakeholders to grasp the urgency."

### Section 7.3: Active vs Inactive
"Here's the activity comparison."

[Run cell]

"The visual contrast really drives home how critical engagement is - nearly twice the churn rate for inactive members."

### Section 7.4: Complaints
[Run cell]

"Look at this dramatic difference - complaints are a major red flag for churn risk."

### Section 7.7: Correlation Heatmap
"This heatmap shows relationships between all our variables."

[Run cell]

"The darker red colors show positive correlations with churn. We can see age, complaints, and inactive status all correlate with higher churn."

### ** LIVE MODIFICATION **
"Let me modify this chart quickly. I'll change the color scheme to make it more readable."

[Modify the code]:
```python
# Change cmap='RdYlGn' to cmap='coolwarm'
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', center=0, ...)
```

[Run cell]

"There - the blue-to-red scheme makes positive and negative correlations clearer."

---

## PART 4: BUSINESS INSIGHTS (2-3 minutes)

### Section 8: Key Findings
"Based on this analysis, here are the actionable insights for the business."

[Run cell - scroll through output]

"I've organized the findings into immediate actions, medium-term strategies, and long-term initiatives.

**Key Takeaways:**
1. [Highest churn geography] needs immediate attention
2. Inactive member engagement is critical
3. Complaint resolution must be prioritized
4. [Age group] demographic needs special focus
5. Product usage patterns reveal opportunities

**Potential Impact:**
If we can reduce churn by just 5 percentage points, we'd retain approximately [X] more customers, representing roughly $[Y] in customer balances."

---

## CONCLUSION (1 minute)

"In summary, this analysis demonstrates how SQL and Python can work together to:
- Extract and aggregate data efficiently
- Clean and analyze patterns
- Visualize insights for stakeholders
- Deliver actionable business recommendations

The combination of technical skills and business thinking is what makes data science valuable. These insights could directly impact the bank's bottom line through improved retention strategies.

I'd be happy to answer any questions or dive deeper into any particular aspect of the analysis."

---

## ANTICIPATED QUESTIONS & ANSWERS

**Q: "How would you improve this analysis?"**
A: "Great question. Next steps would include:
- Building a predictive model to identify at-risk customers before they churn
- Incorporating time-series analysis to spot trends
- A/B testing retention campaigns
- Adding external data like economic indicators or competitor analysis"

**Q: "What other SQL queries would be useful?"**
A: "I'd add:
- Customer lifetime value calculations
- Cohort analysis to track retention over time
- Segment analysis combining multiple factors
- Queries to identify customers matching high-risk profiles"

**Q: "How would you present this to non-technical stakeholders?"**
A: "I'd focus on:
- Executive summary with key numbers
- Simple visuals showing the main story
- Clear dollar impact of recommendations
- Action items prioritized by ROI
- Less technical jargon, more business language"

**Q: "What challenges did you face?"**
A: "The main challenges were:
- Deciding which features were most important to analyze
- Balancing depth vs. clarity in visualizations
- Ensuring SQL queries were optimized for performance
- Translating technical findings into business recommendations"

**Q: "Why this dataset?"**
A: "I chose banking customer churn because:
- It's directly relevant to Capgemini's Financial Services clients
- It demonstrates SQL, Python, and analytical thinking
- It shows I understand business problems, not just technical skills
- The insights are immediately actionable"

---

## TIPS FOR DELIVERY

1. **Pace yourself** - Don't rush, explain your thinking
2. **Engage them** - Make eye contact (if video), pause for questions
3. **Show enthusiasm** - Let your interest in the problem come through
4. **Be ready to improvise** - They might ask to see something specific
5. **Explain trade-offs** - Show you think critically about decisions
6. **Connect to their business** - Mention banks/financial institutions as clients

---

## TROUBLESHOOTING

**If a cell doesn't run:**
"Let me quickly debug this..." [Check the error, explain what went wrong, fix it]

**If they ask to see something not in the notebook:**
"Great question. I can add that analysis right now..." [Write new code live]

**If you're running low on time:**
"I have several more visualizations, but in the interest of time, let me skip to the key business insights..."

---

## FINAL CHECKLIST BEFORE DEMO

□ Notebook opens and all cells run successfully
□ Database file exists and connects properly
□ Charts display correctly
□ You can articulate WHY you made each analytical choice
□ You've practiced the live modifications
□ You know how to quickly add new analyses
□ You have 2-3 follow-up questions ready to ask them

GOOD LUCK! 🚀