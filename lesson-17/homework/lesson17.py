# Lesson 17 homework

# Task 1

# Step 1: Creating the dataframe

import pandas as pd

# Creating the data dictionary
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Step 2: Renaming columns using a Function

# Renaming columns using a function (str.lower + replace spaces with underscore)
df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)

# Step 3: Printing the First 3 Rows

print("First 3 rows of the DataFrame:")
print(df.head(3))

# Step 4: Finding the Mean Age

mean_age = df["age"].mean()
print("Mean age of individuals:", mean_age)

# Step 5: Select and Print only 'first_name' and 'city'

print("Selected columns - first_name and city:")
print(df[['first_name', 'city']])

# Step 6: Adding a new column 'Salary' with random values

import numpy as np

# Adding salary column with random integers between 50,000 and 100,000
df['salary'] = np.random.randint(50000, 100001, size=len(df))

# Step 7: Display summary statistics

print("Summary statistics:")
print(df.describe())

# Task 2

import pandas as pd

# Step 1: Creating the DataFrame

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)
print("Sales and Expenses Data:")
print(sales_and_expenses)

# Step 2: Calculate Maximum sales and expenses

max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()

print("\n Maximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)

# Step 3: Calculate Minimum Sales and Expenses


min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()

print("\n Minimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

# Step 4: Calculate Average(Mean) sales and expenses

avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()

print("\n Average Sales:", avg_sales)
print("Average Expenses:", avg_expenses)

# Task 3

import pandas as pd

# Step1: Creating the DataFrame 
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'], 
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

# Step 2: Set category as the Index

expenses.set_index('Category', inplace=True)
print("Monthly Expenses:")
print(expenses)

# Step 3: Maximum expense for each category (Row-wise)

print("\n Maximum Expense for Each Category:")
print(expenses.max(axis=1))

# Step 4: Minimum expense for each category

print("\n Minimum Expense for Each Category:")
print(expenses.min(axis=1))

# step 5: Average (Mean) expense for each category

print("\n Average Expense for Each Category:")
print(expenses.mean(axis=1))


