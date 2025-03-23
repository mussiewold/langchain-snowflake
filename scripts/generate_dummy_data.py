import pandas as pd
import random

def generate_dummy_data(num_records):
    data = []
    for _ in range(num_records):
        customer_id = f"CUST{random.randint(1000, 9999)}"
        name = f"Customer{random.randint(1, 100)}"
        age = random.randint(18, 70)
        gender = random.choice(['Male', 'Female'])
        tenure = random.randint(1, 72)
        service = random.choice(['Internet', 'Phone', 'Both'])
        monthly_charges = round(random.uniform(20.0, 120.0), 2)
        total_charges = round(monthly_charges * tenure, 2)
        churn = random.choice([True, False])
        data.append([customer_id, name, age, gender, tenure, service, monthly_charges, total_charges, churn])
    
    df = pd.DataFrame(data, columns=['customer_id', 'name', 'age', 'gender', 'tenure', 'service', 'monthly_charges', 'total_charges', 'churn'])
    return df

# Generate 1000 dummy records
df = generate_dummy_data(1000)
df.to_csv('/Users/almazina/dev/db/snowflake/coplitbased/snowflake-genAI/langchain-snowflake/data/dummy_customers.csv', index=False)