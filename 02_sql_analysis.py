import pandas as pd
import sqlite3

# 1. Load the clean data
df = pd.read_csv('../data/cleaned_churn.csv')

# 2. Connect to an SQLite database (a single file)
conn = sqlite3.connect('../churn.db')

# 3. Save our DataFrame to a table in the database called 'customers'
df.to_sql('customers', conn, if_exists='replace', index=False)
print("Data saved to SQLite table 'customers'.")

# --- Let's ask some questions! ---

# Question 1: What is the overall churn rate?
query1 = "SELECT Churn, COUNT(*) as count FROM customers GROUP BY Churn;"
result1 = pd.read_sql_query(query1, conn)
print("\n1. Overall Churn Rate:")
print(result1)

# Question 2: What is the churn rate for different contract types?
query2 = """
SELECT
    Contract,
    COUNT(*) as total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) as churned_customers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2) as churn_rate_percent
FROM customers
GROUP BY Contract
ORDER BY churn_rate_percent DESC;
"""
result2 = pd.read_sql_query(query2, conn)
print("\n2. Churn Rate by Contract Type:")
print(result2)

# Question 3: Do churned customers have different average tenure and charges?
query3 = """
SELECT
    Churn,
    ROUND(AVG(TotalCharges), 2) as avg_total_charges,
    ROUND(AVG(tenure), 1) as avg_tenure_months
FROM customers
GROUP BY Churn;
"""
result3 = pd.read_sql_query(query3, conn)
print("\n3. Average Tenure and Charges for Churned vs. Not Churned:")
print(result3)

# 4. Close the database connection
conn.close()