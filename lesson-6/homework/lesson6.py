# Homework 6

# Task 1 : Modify String with Underscores

def modify_string(txt):
    vowels = "aeiou"
    result = ""
    i = 0
    count = 0
    
    
    while i < len(txt):
        result +=txt[i]
        count += 1
        
        
        # Checking every third character
        if count == 3:
            # Determining if we need to shift
            if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == "_"):
                # Shifting to next character if possible and safe
                if i + 1 < len(txt) and txt[i + 1] !="_":
                    result += txt[i + 1] + "_"
                    i += 1 # Skiping the extra character we just added
                else:
                    # Normal underscore insertion
                    if i + 1 < len(txt): # Only underscore if not at the end
                        result += "_"
                count = 0 # Reset count after handling a chunk
            i += 1
            
            
            
        return result
    
# Results

print(modify_string("hello"))
print(modify_string("assalom"))

# Task 2 Integer Squares Exercise

# Reading input from user

n = int(input())


# Looping from 0 to n-1

for i in range(n):
    print(i ** 2)

# Task 3 Loop-Based Exercises

# Exercise 1: Print first 10 natural numbers using a while loop

i = 1

while i <= 10:
    print(i)
    i += 1


# Exercise 2: Print the following pattern

# Outer loop for rows
for i in range(1,6):
    # Inner loop for numbers in each row
    for j in range(1, i+1):
        print(j, end=" ")
       # Exercise 3:  Calculate sum of all numbers from 1 to a given number

# Reading input from the user
num = int(input("Enter the number:"))

# Initializing sum and counter

total = 0
i = 1

# Adding number from 1 to num

while i <= num:
    total += i
    i += 1
    
# Result

print("Sum is:", total)


    print()  # Move to the next Line

# Exercise 4: Print multiplication table of a given number

# Reading input from the user

num = int(input("Enter a number: "))

# Looping from 1 to 10

for i in range(1,11):
    print(num * i)

# Exercise 5: Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if 70 < num  <200:
        print(num)

# Exercise 6: Count the total number of digits in a number

# Reading number from user

num = int(input("Enter a number:"))

# Initializing digit counter

count = 0

# Handle 0 as a special case

if num == 0:
    count = 1
else:
    
    #Loop until number becomes 0
    while num !=0:
        num = num // 10 # Removes las digit
        count += 1 # Increases counter
        
# Results 
print("Total digits:", count)

# Exercise 7: Print reverse number pattern

n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

# Loop through the list in reverse using index

for i in range(len(list1) -1, -1, -1):
    print(list1[i])


# Exercise 9: Display numbers from -10 to -1 using a for loop

for i in range(-10,0):
    print(i)

# Exercise 10: Display message “Done” after successful loop execution

for i in range(5):
    print(i)
print("Done!")

# Exercise 11: Print all prime numbers within a range

# Defining the range

start = 25
end = 50

print("Prime numbers between", start, "and", end, ":")


# Looping through the range
for num in range(start, end +1):
    if num > 1:
        # Checking if num is divisible by any number from 2 to sqrt(num)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
            
        else:
            print(num)


# Exercise 12: Display Fibonacci series up to 10 terms

# Number of terms 

n = 10

# First two terms
a, b = 0, 1

print("Fibonacci sequence:")

for i in range(n):
    print(a, end=" ")
    a,b = b, a + b

# Exercise 13: Find the factorial of a given number

# Reading the input from the user

num = int(input("Enter a number: "))

# Initializing factorial 

factorial = 1

# Checking if the number is negative 

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("0! = 1")
else:
    for i in range(1, num + 1):
        factorial *=i
    print(f"{num}! = {factorial}")

# Task 4 : Return Uncommon Elements of Lists

from collections import Counter


def get_uncommon_elements(list1, list2):
    # Counts occurences in both lists 
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    # Find differences in both directions
    diff1 = c1 - c2 # Elements only in list 1
    diff2 = c2 - c1 # Elements only in list 2
    
    # Combine the differences and convert to list
    
    result =  list(diff1.elements()) + list(diff2.elements())
    return result

print(get_uncommon_elements([1,1,2], [2,3,4]))

print(get_uncommon_elements([1,2,3], [4,5,6]))

print(get_uncommon_elements([1,1,2,3,4,2], [1,3,4,5]))

