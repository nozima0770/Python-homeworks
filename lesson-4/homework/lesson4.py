# Python Dictionary and Set Exercises

# Dictionary Exercises

# task 1

# Step 1: creating a dictionary

scores ={'Alice': 88, 'Bob': 95, 'Charlie':70, 'Diana': 82}

# Step 2: Sorting by value in asc order

asc_sorted = dict(sorted(scores.items(), key=lambda item: item[1]))

# Step 3: Sorting by value in desc order

desc_sorted = dict(sorted(scores.items(), key=lambda item: item[1], reverse = True))

# Results 

print("Ascending by value:", asc_sorted)
print("Descending by value:", desc_sorted)

# task 2

# Step 1: creating the sample dictionary

my_dict = {0: 10, 1: 20}

# Step 2 : adding a new key-value pair

my_dict[2] = 30

# Result

print(my_dict)

# task 3

# step 1: defining the sample dictionaries

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


# step 2: concatenating them using unpacking

merge_dict = {**dic1, **dic2, **dic3}

# Results 

print(merge_dict)


# task 4

# Step 1: setting the value of n

n = 5

# Step 2: generating the dictinary using a loop

squares_dict = {x:x*x for x in range(1, n+1)}

# Result

print(squares_dict)


# task 5

# Step 1: generating dictionary using dictionary comprehension

squares_dict = {x:x*x for x in range(1,16)}

# Result

print(squares_dict)

# Set exercises

# task 1

# Method 1: using curly braces

my_set = {1, 2, 3, 4, 5}

# Method 2: using the set () function

another_set = set(["apple", "banana", "cherry"])

# results

print("set of numbers:", my_set)
print("Set of fruits:", another_set)

# task 2

# Step 1: creating a set

colors = {"red", "green", "blue", "yellow"}

# Step 2: Iterate over the set using a for loop

for color in colors:
    print(color)


# task 3

# Step 1: creating an empty set

my_set = set()

# step 2: adding a single item

my_set.add("apple")

# step 3: adding a multiple items

my_set.update(["banana", "cherry", "orange"])

# result

print(my_set)


# task 4

# Step 1: creating a set

fruits = {"apple", "banana", "cherry", "orange"}

# Step 2: removing an item using remove()

fruits.remove("banana")

# Step 3: removing an item using discard()

fruits.discard("cherry")

# Step 4: removing an item using pop()

removed_item = fruits.pop()

# Results

print("After removals:", fruits)
print("Popped item:", removed_item)

# Step 6: clear the set

fruits.clear()

print("After clear:", fruits)


# task 5

# Step 1: creating a set

my_set = {"apple", "banana", "cherry"}

# Step 2 : defining the item to remove

item_to_remove = "banana"

# Step 3: removing the item if it is present

my_set.discard(item_to_remove)

# result

print(my_set)
