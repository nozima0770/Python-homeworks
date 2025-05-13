#  task 1

fruits = ["apple", "banana", "cherry", "orange", "mango"]
print(fruits[2])

# task 2

# Step 1. Creating two lists of numbers
list1 = [1,2,3]
list2 = [4,5,6]

# Step 2. Concatenating the two lists.

combined_list = list1 + list2

# Result

print(combined_list)

# task 3

numbers = [4, 8, 15, 16, 23, 42]

# Step 2: extracting first, middle, and last elements

first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]

# Step 3: Storing in a new list

extracted = [first, middle, last]

# Result

print(extracted)

# task 4

# Step 1: creating a list of favorite movies

favorite_movies = ["Day and Night", "Last", "Black Love", "Chalikusu"]

# Step 2: Converting the list to a tuple

movies_tuple = tuple(favorite_movies)

# Printing the tuple

print(movies_tuple)

# task 5

# Step 1: creating alist of cities

cities = ["London", "New York", "Tokyo", "Paris", "Berlin"]

# Step 2: check if "Paris" is in the list

is_paris_in_list = "Paris" in cities

# Result

print(is_paris_in_list)

# task 6

# Step 1: creating a list of numbers

numbers = [1, 2, 3, 4, 5]

# Step 2 : Duplicating the list without using loops

duplicated_list = numbers * 2 

# Result

print(duplicated_list)

# task 7

numbers = [10, 20, 30, 40, 50]

# Swaping the first and last elements

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

# task 8

numbers = [1,2,3,4,5,6,7,8,9,10]
slice_result = numbers[3:7]

print(slice_result)

# task 9

colors = ["red", "blue", "green", "blue", "yellow", "blue"]
blue_count = colors.count("blue")

print(blue_count)

# task 10

animals = ("cat", "dog", "elephant", "lion", "tiger")
lion_index = animals.index("lion")

print(lion_index)

# task 11

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

merged_tuple = tuple1 + tuple2

print(merged_tuple)

# task 12

my_list = [10, 20, 30, 40]
my_tuple = ("a", "b", "c")

list_length = len(my_list)
tuple_length = len(my_tuple)

print("Length of list:", list_length)
print("Length of tuple:", tuple_length)

# task 13

numbers_tuple = (10, 20, 30, 40, 50)
numbers_list = list(numbers_tuple)

print(numbers_list)

# task 14

numbers = (12, 45, 7, 89, 23, 56)

maximum = max(numbers)
minimum = min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)

# task 15

words = ("apple", "banana", "cherry", "date", "elderberry")

reversed_words = words[::-1]

print(reversed_words)
