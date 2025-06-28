# Lesson 19 homework

# Homework 1: Analyzing Sales Data

import pandas as pd

# Loading the dataset
df = pd.read_csv("C:\\Users\\User\\Desktop\\Python lessons\\sales_data.csv")

# Checking the first few rows
print(df.head())

# Group by 'Category' and calculate required stats
# Step 1
category_stats = df.groupby('Category').agg(
    total_quantity_sold=('Quantity', 'sum'),
    average_price=('Price', 'mean'),
    max_quantity_single_transaction=('Quantity', 'max')
)

print("Aggregate stats by Category:")
print(category_stats)

# Step 2: Identify the top-selling product in each category

# Group and sum quantity

product_sales = df.groupby(['Category', 'Product']) ['Quantity'].sum().reset_index()

# For each category , find the product with the max quantity

top_selling_products = product_sales.sort_values(['Category', 'Quantity'], ascending=[True, False]).drop_duplicates('Category')

print("Top-selling product in each category:")
print(top_selling_products)

# Step 3: Find the date on which the highest total sales (quantity * price) occurred.

# Creating total sale column
df['TotalSale'] = df['Quantity'] * df['Price']

# Group by Date and sum total sales

sales_by_date = df.groupby('Date')['TotalSale'].sum()

# Find the date with the highest sales

best_sales_date = sales_by_date.idxmax()
highest_sales_amount = sales_by_date.max()

print(f"Highest total sales occured on: {best_sales_date} with ${highest_sales_amount:.2f}")

# Homework 2: Examining Customer Orders

import pandas as pd 

# Loading the dataset
df = pd.read_csv("C:\\Users\\User\\Desktop\\Python lessons\\customer_orders.csv")

# preview the first few rows

print(df.head())

# Task 1: Filter customers who made at least 20 orders

# Count orders per customer
customer_order_counts = df.groupby('CustomerID')['OrderID'].nunique()

# get customer IDs with at least 20 orders
active_customers = customer_order_counts[customer_order_counts >= 20].index

# Filter original DataFrame
df_active_customers = df[df['CustomerID'].isin(active_customers)]

print("Customers with at least 20 orders:")
print(df_active_customers['CustomerID'].unique()) 

# Task 2: Identify customers who ordered products with avg price > $120

# Group by customer and calculate their average price
high_value_customers = df.groupby('CustomerID')['Price'].mean()

# Filter customers whose avg price per unit > $120
high_value_customers = high_value_customers[high_value_customers > 120].index

# Filter the main DataFrame
df_high_value = df[df['CustomerID'].isin(high_value_customers)]

print("Customers with avg product price > $120:")
print(df_high_value['CustomerID'].unique())

# Task 3: Total quantity and total price per product, filter by quantity >= 5

# step 1: Calculate total quantity and total revenue per product

product_summary = df.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_revenue=('Price', lambda x: (x * df.loc[x.index, 'Quantity']).sum())
)

# step 2: Filter products with total quantity >=5

filtered_products = product_summary[product_summary['total_quantity'] >= 5]

print("Products with total quantity >= 5:")
print(filtered_products)

# Homework Assignment 3: Population Salary Analysis

import pandas as pd
import sqlite3

# Step 1: Load population data from SQLite

# Connect to SQLite DB
conn = sqlite3.connect(r"C:\Users\User\Desktop\Python lessons\population.db")

# Load data from 'population' table
df_pop = pd.read_sql("SELECT * FROM population", conn)

# Preview the data
print(df_pop.head())

# Step 2:  Load salary band definitions from Excel


df_bands = pd.read_excel(r"C:\Users\User\Desktop\Python lessons\population_salary_analysis.xlsx")

# View the first few rows to confirm
print(df_bands.head())

# Step 3: map each person to a salary band

# making sure bands are sorted

df_bands = df_bands.sort_values("Min Salary").reset_index(drop=True)

# Creating interval list

bins = list(df_bands['Min Salary']) + [df_bands['Max Salary'].iloc[-1] +1]
labels = df_bands['Salary Band']

# Creating a new column for salary category
df_pop['Salary Band'] = pd.cut(df_pop['salary'], bins=bins, labels=labels, right=False)


print(df_pop[['salary', 'Salary Band']].head())

# step 4: 
grouped = df_pop.groupby('Salary Band')

# Total population count
total_population = len(df_pop)

# Calculate all measures
summary = grouped['Salary'].agg(
    Population='count',
    Average_Salary='mean',
    Median_Salary='median'
).reset_index()

# Add % of population
summary['Percent_of_Population'] = (summary['Population'] / total_population) * 100

print(summary)

grouped_state = df_pop.groupby(['State', 'Salary Band'])

summary_state = grouped_state['Salary'].agg(
    Population='count',
    Average_Salary='mean',
    Median_Salary='median'
).reset_index()

# Total population per state
state_totals = df_pop.groupby('State')['Salary'].count().reset_index(name='State_Total')

# Merge for % calculation
summary_state = summary_state.merge(state_totals, on='State')

summary_state['Percent_of_Population'] = (
    summary_state['Population'] / summary_state['State_Total'] * 100
)

# Drop helper column if desired
summary_state.drop(columns='State_Total', inplace=True)

print(summary_state)

