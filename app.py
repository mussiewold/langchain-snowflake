import streamlit as st
import pandas as pd
# from langchain_openai import OpenAI
# from scripts import semantic_search
# from openai import OpenAI
# from scripts.semantic_search import semantic_search
import os 
from langchain.chat_models import init_chat_model
from matplotlib import pyplot as plt

import openai 

st.set_page_config(layout="wide")

# Load the dummy data
openai.api_key=os.environ.get("OPENAI_API_KEY")
df = pd.read_csv('data/dummy_customers.csv')

# Streamlit app
st.title("Telecom Customer Data")

# Display the data
st.write("Customer Data", df)

# Analyze customer churn
churned_customers = df[df['churn'] == True]
st.write("Churned Customers", churned_customers)


customers_above_50 = churned_customers[churned_customers['age'] > 50]
age_summary = customers_above_50['age'].describe()

# Convert this summary to a text format to send to the model
summarized_info = f"Summary of customers above 50 years old:\n{age_summary}\nChurned customers in this group: {customers_above_50.sum()}"


# GhatGPT integratioin 
st.header("Chat with GPT-3 about churned customers")
chat_input = st.text_input("You: Ask a quesiton about churned customers")

if chat_input:
   
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # prompt=prompt,
        messages=[
            {"role": "system", "content": "You are a telecom analyst."},
            {"role": "system", "content": "You are analyzing customer churn."},
            {"role": "user", "content": f"Customer churn analysis: {summarized_info}\n\n{chat_input}"}
        ],
        max_tokens=100,
        temperature=0
    )
    st.write(f"GPT-3: {response['choices'][0]['message']['content'].strip()}")


# Filter by age and predict the number of cutomers likely to churn 
st.header("Predict churn based on age")
age_filter = st.slider("Select age range", min_value=int(df['age'].min()), max_value=int(df['age'].max()), value=(50, 70))
filtered_customers = df[(df['age'] >= age_filter[0]) & (df['age'] <= age_filter[1])]
# // Display the filtered customers
st.write("Filtered Customers", filtered_customers)

# Predict the number of customers likely to churn
num_churned = len(filtered_customers[filtered_customers['churn'] == True])
st.write(f"Number of customers likely to churn: {num_churned}")


# Compare this snippet from scripts/semantic_search.py:
# # from langchain.chains import LLMChain
st.header("Predict churn based on monthly charges")
monthly_charges_filter = st.slider("Select monthly charges range", min_value=int(df['monthly_charges'].min()), max_value=int(df['monthly_charges'].max()), value=(0, 100))
filtered_customers = df[(df['monthly_charges'] >= monthly_charges_filter[0]) & (df['monthly_charges'] <= monthly_charges_filter[1])]
# Display the filtered customers
st.write("Filtered Customers", filtered_customers)

# # from langchain.chains import LLMChain
# Create a pie chart based on age groups 
st.header("Customer Distribution by Age Groups")
age_groups = {
    '18-24':df[(df['age'] >= 18) & (df['age'] <= 24)].shape[0],
    '25-34':df[(df['age'] >= 25) & (df['age'] <= 34)].shape[0], 
    '35-44':df[(df['age'] >= 35) & (df['age'] <= 44)].shape[0],
    '45-54':df[(df['age'] >= 45) & (df['age'] <= 54)].shape[0],
    '55-64':df[(df['age'] >= 55) & (df['age'] <= 64)].shape[0],
    '65+':df[(df['age'] >= 65)].shape[0]
}

fig, ax = plt.subplots() 
ax.pie(age_groups.values(), labels=age_groups.keys(), autopct='%1.1f%%', startangle=90)
ax.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig)
# Compare this snippet from scripts/semantic_search.py:

# Example Questions to Ask the Model:
# "How many of the customers above 50 will likely churn in the next month?"
# "Predict the churn rate for customers aged over 50."
# "Based on this data, what is the estimated number of churns from customers over 50 in the next quarter?"
# Make sure that the prompt you send to the model contains enough context and is clear for prediction tasks. You might also want to include additional details about trends, previous churn rates, or any other relevant data if available.


# streamlit run app.py --server.headless=false

st.experimental_singleton.clear()  # Clears singleton cache
st.experimental_memo.clear()  # Clears memo cache
