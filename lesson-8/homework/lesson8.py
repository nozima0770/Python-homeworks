# Lesson 8 homework
# Exception Handling Exercises
# task 1 ZeroDivisionError

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# task 2 ValueError

try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That's not a valid integer.")

# task 3 FileNotFoundError

try:
    with open("noneexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")

# task 4  TypeError

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    result = float(a) + float(b)
except ValueError:
    print("Invalid input. Please enter numbers.")
except TypeError:
    print("Type error occured.")

# task 5 PermissionError

try:
    with open("/root/secret.txt","r") as file:
        content = file.read()
except PermissionError:
    print("You do not have permission to access this file.")

# task 6 Index Error 

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index is out of range.")

# task 7 KeyboardInterrupt

try:
    number = input("Enter a number (press Ctrl+C to cancel): ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

# task 8 ArithmeticError

try:
    result = 10 / 0
except ArithmeticError:
    print("Arithmetic error occured.")

# task 9 UnicodeDecodeError

try: 
    with open("utf16_file.txt", encoding = "utf - 8") as file:
        content = file.read()
except UnicodeDecodeError:
    print("Encoding issue. Cannot decode the file with UTF-8.")

# task 10 AttributeError

try:
    my_list = [1,2,3]
    my_list.upper()
except AttributeError:
    print("List object has no method 'upper'.")

# Python File Input Output: Exercises, Practice, Solution
# File Input/Output Exercises

# task 1 Read an entire text file

with open(r"C:\Users\User\Desktop\CSV.txt", "r") as file:
    content = file.read()
    print(content)

# task 2 Read first n lines of a file

n = 3
with open(r"C:\Users\User\Desktop\CSV.txt", "r") as file:
    for i in range(n):
        print(file.readline().strip())

# task 3 Append text to a file and display it

with open(r"C:\Users\User\Desktop\CSV.txt", "a") as file:
    file.write("\nNew line added.")
    
with open(r"C:\Users\User\Desktop\CSV.txt", "r") as file:
    print(file.read())

# task 4 Read last n lines of a file

n = 3
with open(r"C:\Users\User\Desktop\CSV.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line.strip())

# task 5 Read file line by line and store it into a list

with open(r"C:\Users\User\Desktop\CSV.txt", "r") as file:
    lines_list = file.readlines()
print(lines_list)

# task 6 Read file line by line and store into a variable

with open(r"C:\Users\User\Desktop\CSV.txt", "r") as file:
    content = "".join(file.readlines())
print(content)

# task 7 Read file line by line into an array (same as list in Python)

with open(r"C:\Users\User\Desktop\CSV.txt", "r") as file:
    lines_array = [line.strip() for line in file]
print(lines_array)

# task 8 Find the longest word(s)

with open(r"C:\Users\User\Desktop\CSV.txt", "r") as file:
    words = file.read().split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
print("Longest words:", longest_words)

# task 9 Count number of line in a text file

with open (r"C:\Users\User\Desktop\CSV.txt", "r") as file:
    line_count = sum(1 for _ in file)
print("Total lines:", line_count)


# task 10 Count frequency of words

from collections import Counter

with open(r"C:\Users\User\Desktop\CSV.txt", "r") as file:
    words = file.read().replace(',', '').split()
    word_freq = Counter(words)
print(word_freq)

# task 11 Get file size

import os
file_size = os.path.getsize(r"C:\Users\User\Desktop\CSV.txt")
print("File size:", file_size, "bytes")

# task 12 Write a list to a file

my_list = ["apple", "banana", "cherry"]
with open(r"C:\Users\User\Desktop\CSV.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")

# task 13 Copy contents of one file to another

with open (r"C:\Users\User\Desktop\CSV.txt", "r") as src, open(r"C:\Users\User\Desktop\Products (2).txt", "w") as dest:
    dest.write(src.read())


# task 14 Combine lines from two files 

with open(r"C:\Users\User\Desktop\CSV.txt", "r") as f1, open(r"C:\Users\User\Desktop\Products (2).txt", "r") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

# task 15 Read a random line from a file

import random

with open(r"C:\Users\User\Desktop\Products (2).txt", "r") as file:
    lines = file.readlines()
    print(random.choice(lines).strip())

# task 16 Check if a file is closed

file = open(r"C:\Users\User\Desktop\Products (2).txt", "r")
print("Is closed?", file.closed)
file.close()
print("Is closed after closing?", file.closed)

# task 17 Remove new line characters 

with open(r"C:\Users\User\Desktop\Products (2).txt", "r") as file:
    lines = file.readlines()
    cleaned = [line.strip() for line in lines]
print(cleaned)

# task 18 Count words in a file( handle commas)

with open(r"C:\Users\User\Desktop\Products (2).txt", "r") as file:
    text = file.read().replace(",", " ")
    words = text.split()
print("Word count:", len(words))

# task 19 Extract characters from multiple files into a list

import glob

char_list = []
for filename in glob.glob("*.txt"):
    with open(filename, "r") as file:
        char_list.extend(list(file.read()))
print(char_list)

# task 20 Generate 26 text files A.txt to Z.txt

import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is file {letter}.txt")

# task 21 Alphabet file with specified letters per line

import string

letters_per_line = 5
alphabet = string.ascii_uppercase

with open("alphabet.txt", "w") as file:
    for i in range(0, len(alphabet), letters_per_line):
        file.write("".join(alphabet[i:i+letters_per_line]) + "\n")

