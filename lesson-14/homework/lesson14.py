# Lesson 14 homework

# Task 1: JSON Parsing

import json

sample_data = [
    {"name": "Alice", "age": 20, "major": "Computer Science"},
    {"name": "Bob", "age": 22, "major": "Mathematics"}
]

with open("students.json", "w") as f:
    json.dump(sample_data, f, indent=4)

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

# Task 2: Weather API

import requests

API_KEY = "5d32683450ae6f56f2eb9c9f6d9151af"
city = "Tashkent"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(f"City: {city}")
print(f"Temperature: {data['main']['temp']}°C")
print(f"Humidity: {data['main']['humidity']}%")
print(f"Weather: {data['weather'][0]['description']}")

# Task 3: JSON Modification

import json

# Sample initial data for the JSON file
books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
]

# Write to books.json
with open("books.json", "w") as f:
    json.dump(books, f, indent=4)

print("books.json file created successfully.")

import json

def load_books():
    with open("books.json", "r") as file:
        return json.load(file)

def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    books = load_books()
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = int(input("Enter year: "))
    books.append({"title": title, "author": author, "year": year})
    save_books(books)

def update_book():
    books = load_books()
    title = input("Enter title to update: ")
    for book in books:
        if book["title"] == title:
            book["author"] = input("New author: ")
            book["year"] = int(input("New year: "))
            break
    save_books(books)

def delete_book():
    books = load_books()
    title = input("Enter title to delete: ")
    books = [book for book in books if book["title"] != title]
    save_books(books)

# Example menu
while True:
    choice = input("1. Add 2. Update 3. Delete 4. Exit: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        break

# Task 4

import requests
import random

API_KEY = "62eb3f0a"
genre = input("Enter movie genre (e.g. Action, Comedy, Drama): ")

# Fixed list of popular movie titles
movie_titles = ["Inception", "Titanic", "Avengers", "Joker", "The Matrix"]

random.shuffle(movie_titles)

found = False

for title in movie_titles:
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # raises exception for 4xx/5xx
        data = response.json()

        # Check if movie is found
        if data.get("Response") == "True":
            if genre.lower() in data.get("Genre", "").lower():
                print(f"\n Title: {data['Title']}")
                print(f" Genre: {data['Genre']}")
                print(f" Plot: {data['Plot']}")
                found = True
                break
        else:
            print(f" Movie '{title}' not found in OMDb.")

    except requests.exceptions.RequestException as e:
        print(" Network error:", e)
        break
    except ValueError:
        print(" Failed to decode JSON response.")
        break

if not found:
    print("\n No movie found in that genre.")
