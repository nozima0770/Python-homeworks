#  Task 1 Create your own virtual environment and install some python packages.
# python -m venv myenv
# .\myenv\scripts\activate
# pip install numpy

# Task 2 Create custom modules

# math_operations.py

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b (a-b)."""
    return a - b 

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b): 
    """Returns the result of dividing a by b. raises error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# creating new file main.py

import math_operations as mo
    
print(mo.add(10,5))
print(mo.subtract(10,5))
print(mo.multiply(10,5))
print(mo.divide(10,5))

# Task 2 Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)


# Step 1: Creating the file string_utils.py

# Step 2: Adding the following code inside string_utils.py

def reverse_string(s):
    """Returns the reverse of the input string."""
    return s[::-1]

def count_vowel(s):
    """Counts the number of vowels in the input string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Step 3: How to use this module in another file

import string_utils as su

print(su.reverse_string("Hello"))
print(su.count_vowel("Hello World"))


# Task 3: Create custom packages

# Step 1: Creating Package Structure

# I'm working in a folder my_project.
# Creating package folders, creating __init__.py in each folder, adding module files.

# geometry/circle.py

import math

def calculate_area(radius):
    """Returns the area of a circle given its radius."""
    return math.pi * radius ** 2

def calculate_circumference(radius):
    """Returns the circumference of a circle given its radius."""
    return 2 * math.pi * radius

# geometry/__init__.py

from .circle import calculate_area, calculate_circumference

# file_operations/file_reader.py

def read_file(file_path):
    """Reads and returns the content of the file at the given path."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
# file_operations/file_writer.py

def write_file(file_path, content):
    """Writes the given content to the file at the specified path."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# file_operations/__init__.py

from .file_reader import read_file
from .file_writer import write_file

# Example usage in the root folder
# main.py

from geometry.circle import calculate_area, calculate_circumference
from file_operations import read_file, write_file

# Geometry usage
radius = 5
print("Area:", calculate_area(radius))
print("Circumference:", calculate_circumference(radius))

# File Operations usage
write_file("example.txt", "Hello from custom package!")
content = read_file("example.txt")
print("File Content:", content)

