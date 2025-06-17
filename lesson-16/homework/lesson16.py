# Lesson 16 homework

# Task 1: Convert List to 1D Array

import numpy as np

# Original list

my_list = [12.23, 13.32, 100, 36.32]
print("Original List:", my_list)

# Convert to NumPy array

array_1d = np.array(my_list)
print("One-dimensional NumPy array:", array_1d)

# Task 2: Create 3x3 Matrix (2?10)

matrix = np.arange(2,11).reshape(3, 3)
print(matrix)

# Task 3: Null Vector (10) & Update Sixth Value

# Null vector of size 10

null_vector = np.zeros(10)
print("Null Vector:", null_vector)

# Update the 6th element (index 5)
null_vector[5] = 11
print("Update Vector:", null_vector)

# Task 4: Array from 12 to 38

array_range = np.arange(12, 38)
print(array_range)

# Task 5: Convert Array to Float Type

int_array = np.array([1, 2, 3, 4])
float_array = int_array.astype(float)
print("Original array:", int_array)
print("Float array:", float_array)

# Task 6: Celsius to Fahrenheit Conversion

celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = (celsius * 9/5) + 32

print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0. ])
fahrenheit = (celsius * 9/5) + 32

print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

# Task 7: Append Values to Array (Do self-tudy)

import numpy as np

# Original array
original_array = np.array([10, 20, 30])
print("Original array:", original_array)

# Append values
new_array = np.append(original_array, [40, 50, 60, 70, 80, 90])
print("After appending:", new_array)

# Task 8: Array Statistical Functions (Do self-study)

# Random array of 10 elements between 0 and 100
random_array = np.random.randint(0, 100, size = 10)
print("Random array:", random_array)

# Statistical functions
mean_value = np.mean(random_array)
median_value = np.median(random_array)
std_dev = np.std(random_array)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standart Deviation:", std_dev)

# Task 9: Find min and max

# 10*10 array with random values between 0 and 100
array_10x10 = np.random.randint(0, 100, size=(10,10))
print("10x10 array:\n", array_10x10)

# Find min and max
min_val = np.min(array_10x10)
max_val = np.max(array_10x10)

print("Minimum value:", min_val)
print("Maximum value:", max_val)

# Task 10: Create a 3x3x3 array with random values.

array_3x3x3 = np.random.rand(3, 3, 3)
print("3x3x3 Random Array:\n", array_3x3x3)
