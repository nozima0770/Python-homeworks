# Homework 5

# Task 1

def is_leap(year):
    # Determines whether a given year is a leap year.
    # A year is a leap year if:
    # It is dividible by 4, and
    # It is not divisible by 100, unless it is also dividible by 400.
    
    # Parameters:
    # year(int): The year to be checked.
    
    # Returns:
    # bool: True if the year is a leap year, False otherwise.
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap(2020))
print(is_leap(1900))


# Task 2

# Step 1: taking input from user and converting to integer

n = int(input("Enter a number between 1 and 100"))

# Step 2: applying conditions

if n % 2 == 1:  # odd number
    print("Weird")
elif n % 2 == 0 and 2 <= n <=5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

# Task 3

# Here we sure then a is smaller than b, then use range() starting from the next even number:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# We make sure to use the correct order

if a > b:
    a,b = b,a
    
    
start = a if a % 2 == 0 else a+1

even_numbers = list(range(start, b + 1, 2))

print("Even numbers:", even_numbers)

# Task 3(2)

# Solution 2 - No if, no else, no loop

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a,b = sorted((a,b))  # ensures a<=b
start = a + (a % 2) # if a is odd, adds 1; if even,stays the same


even_numbers = list(range(start, b + 1, 2))

print("Even numbers:", even_numbers)
