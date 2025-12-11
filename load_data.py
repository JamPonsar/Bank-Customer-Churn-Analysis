"""
Load bank customer churn data into SQLite database
"""
import pandas as pd
import sqlite3
import os

# File paths
csv_path = 'data/Customer-Churn-Records.csv'
db_path = 'data/bank_churn.db'

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Load CSV
print("Loading CSV data...")
df = pd.read_csv(csv_path)
print(f"Loaded {len(df)} customer records")

# Create SQLite database
print("\nCreating SQLite database...")
conn = sqlite3.connect(db_path)

# Load data into database
df.to_sql('customers', conn, if_exists='replace', index=False)
print(f"Data loaded into 'customers' table in {db_path}")

# Verify the data
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM customers")
count = cursor.fetchone()[0]
print(f"Verified: {count} records in database")

# Show table schema
print("\nTable Schema:")
cursor.execute("PRAGMA table_info(customers)")
schema = cursor.fetchall()
for col in schema:
    print(f"  {col[1]} ({col[2]})")

conn.close()
print("\n✓ Database setup complete!")