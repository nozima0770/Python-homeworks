# Lesson 21 homework

# DataFrame 1: Student Grades

import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Ex 1: Average grade per student

df1["Average"] = df1[["Math", "English", "Science"]].mean(axis=1)
print("Average grades for each student:")
print(df1[["Student_ID", "Average"]])

# Ex2: Student with the highest average grade

top_student = df1.loc[df1["Average"].idxmax()]
print("\nStudent with the highest average grade:")
print(top_student)

# Ex3: Total marks per student
df1["Total"] = df1[["Math", "English", "Science"]].sum(axis=1)
print("\nTotal marks for each student:")
print(df1[["Student_ID", "Total"]])

#Ex4: Bar chart of average grades in each subject

subject_averages = df1[["Math", "English", "Science"]].mean()

subject_averages.plot(kind="bar", color=["skyblue", "lightgreen", "salmon"])
plt.title("Average Grades by Subject")
plt.ylabel("Average Grade")
plt.xlabel("Subject")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# DataFrame 2: Sales Data

import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# Ex 1: Total Sales for each product

total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Total sales for each product:\n", total_sales)

# Ex 2: Date with the highest total sales

df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
print("Date with highest total sales:", max_sales_date)

# Ex 3: Percentage change in sales from previous day

percent_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
print("Percentage change in sales:\n", percent_change)

# Ex 4: Line chart of sales trends

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

for product in ['Product_A', 'Product_B', 'Product_C']:
    plt.plot(df2['Date'], df2[product], label=product)
    
plt.title("Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# DataFrame 3: Employee Information

import pandas as pd

import matplotlib.pyplot as plt

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Ex 1: Average salary for each department
avg_salary = df3.groupby('Department')['Salary'].mean()
print("Average salary per department:\n", avg_salary)

# Ex 2: Employee with the most experience

most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
print("\nMost experienced employee:\n", most_experienced)

# Ex 3: Add 'Salary Increase' column from minimum salary

min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary) * 100

# Ex 4: Bar chart - Employee count per department

dept_counts = df3['Department'].value_counts()

plt.figure(figsize=(8, 5))
dept_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Employee Count per Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# DataFrame 4: Customer Orders

import pandas as pd

import matplotlib.pyplot as plt


data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# Ex 1: Total revenue

total_revenue = df4['Total_Price'].sum()
print("Total Revenue: $", total_revenue)

# Ex 2: Most ordered product

most_ordered_product = df4.groupby('Product')['Quantity'].sum().idxmax()
print("Most ordered product:", most_ordered_product)

# Ex 3: Average quantity ordered

average_quantity = df4['Quantity'].mean()
print("Average quantity ordered:", round(average_quantity, 2))

# Ex 4: Pie chart of sales distribution per product

product_sales = df4.groupby('Product')['Total_Price'].sum()

plt.figure(figsize=(6,6))
product_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors =['g', 'b', 'r'])
plt.title("Sales Distribution by Product")
plt.ylabel("") # Hide y-axis label
plt.tight_layout()
plt.show()
