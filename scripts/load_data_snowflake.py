import snowflake.connector
import pandas as pd
import os 

# Load the dummy data
df = pd.read_csv('/Users/almazina/dev/db/snowflake/coplitbased/snowflake-genAI/langchain-snowflake/data/dummy_customers.csv')

# Connect to Snowflake using environment variables
conn = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT')
)
# Create a cursor object
cur = conn.cursor()

# Use the database and schema
cur.execute("USE DATABASE telecom_db")
cur.execute("USE SCHEMA telecom_schema")

# Load data into the table
for index, row in df.iterrows():
    cur.execute(f"""
        INSERT INTO customers (customer_id, name, age, gender, tenure, service, monthly_charges, total_charges, churn)
        VALUES ('{row['customer_id']}', '{row['name']}', {row['age']}, '{row['gender']}', {row['tenure']}, '{row['service']}', {row['monthly_charges']}, {row['total_charges']}, {row['churn']})
    """)

# Commit the transaction
conn.commit()

# Close the connection
cur.close()
conn.close()