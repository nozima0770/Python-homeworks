# Lesson 9 homework

# Object-Oriented Programming (OOP) Exercises

# task 1 Circle Class



import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

# Create the object
circle1 = Circle(5)

# Test output
print("Radius:", circle1.radius)
print("Area:", circle1.area())
print("Perimeter:", circle1.perimeter())

# task 2 Person Class

from datetime import datetime

class Person:
    def __init__ (self, name, country, date_of_birth):
        self.name = name
        self.country = country
        # Expecting date_of_birth as a string in 'YYYY-MM-DD' format
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
        
    def get_age(self):
        """Calculate and return the person's age in years."""
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        
        # Adjusting if birthday hasn't occured yet this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
            
        return age
    
# Example usage
person1 = Person("Alice", "USA", "1990-06-15")


print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth.strftime('%Y-%m-%d'))
print("Age:", person1.get_age())

# task 3 Calculator Class

class Calculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b
    
    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b
    
    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b
    
    def divide(self, a, b):
        """Return the division of a by b. Handle division by zero."""
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    
# Example usage 
calc = Calculator()

print("Add:", calc.add(10, 5))
print("Subtract:", calc.subtract(10, 5))
print("Multiply:", calc.multiply(10, 5))
print("Divide:", calc.divide(10, 5))
print("Divide by 0:", calc.divide(10, 0)) 

# task 4 Shape and Subclasses

import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    
# Subclass for Circle

class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
# Subclass for Square

class Square(Shape):
    def __init__ (self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    
    
# Subclass for Triangle (assuming all 3 sides are given, Heron's formula )

class Triangle(Shape):
    def __init__ (self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        # Heron's Formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    
# Example usage 

circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print("Circle - Area:", circle.area(), "| Perimeter:", circle.perimeter())
print("Square - Area:", square.area(),"| Perimeter:", square.perimeter())
print("Triangle - Area:", triangle.area(),"| Perimeter:", triangle.perimeter())


# task 5 Binary Search Tree Class

class Node:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__ (self):
        self.root = None
        
    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
            
    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)
            # If value == current_node.value, do nothing (no duplicates)
            
    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)
        
        
# Example usage 
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Search 40:", bst.search(40))
print("Search 90:", bst.search(90))


# task 6 Stack Data Structure


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)

print("Top item:", stack.peek())     
print("Size:", stack.size())         
print("Popped:", stack.pop())    

# task 7 Linked List Data Structure

# Node class to represent each element in the list

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        
        
# LinkedList class

class LinkedList:
    def __init__ (self):
        self.head = None
        
    def insert (self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def delete(self, key):
        """Delete the first node with the given data (key)."""
        current = self.head
        
        # If head node is to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
            
        # If key was not found 
        if current is None:
            return "Value not found."
        
        # Unlike the node
        prev.next = current.next
        current = None
        
    def display(self):
        """Print all elements in the list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)
        
        
# Example usage 

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()

ll.delete(20)
ll.display()

ll.delete(100)

# task 8 Shopping Cart Class

class ShoppingCart:
    def __init__(self):
        self.items = {} # Dictionary to store items: {item_name:[quantity, price]}
        
    def add_item(self, name, quantity, price):
        """Add or update an item in the cart."""
        if name in self.items:
            self.items[name][0] += quantity # Update quantity
        else:
            self.items[name] = [quantity, price]
            
    def remove_item(self, name):
        """Remove an item from the cart."""
        if name in self.items:
            del self.items[name]
        else:
            print(f"Item '{name}' not found in the cart.")
            
    def calculate_total(self):
        """Calculate the total price of all items."""
        total = 0
        for quantity, price in self.items.values():
            total += quantity * price
        return total
    
    def show_cart(self):
        """Display all items in the cart."""
        if not self.items:
            print("your shopping cart is empty.")
        else:
            print("Items in your cart:")
            for name, (quantity, price) in self.items.items():
                print(f"- {name}: {quantity} x ${price:.2f}")
                
                
# Example usage

cart = ShoppingCart()
cart.add_item("Apples", 2, 1.50)
cart.add_item("Bread", 1, 2.00)
cart.add_item("Milk", 3, 1.20)

cart.show_cart()
print("Total Price: $, cart.calculate_total()")

cart.remove_item("Bread")
cart.show_cart()
print("Total Price after removal: $", cart.calculate_total())    


# task 9 Stack with Display

class Stack:
    def __init__ (self):
        self.items = []
        
    def push(self, item):
        """Add an item to the stack."""
        self.items.append(item)
        print(f"Pushed: {item}")
        
    def pop(self):
        """Remove and return the top item of the stack."""
        if not self.is_empty():
            popped = self.items.pop()
            print(f"Popped: {popped}")
            return popped
        else:
            print("Stack is empty. Nothing to pop.")
            return None
        
    def display(self):
        """Display all items in the stack."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):")
            for item in reversed(self.items):
                print(item)
                
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    
# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()

stack.pop()
stack.display()

# task 10 Queue Data Structure

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty. Nothing to dequeue.")
            return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def display(self):
        """Display all items in the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue (front to back):", self.items)

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()

queue.dequeue()
queue.display()

# task 11 Bank Class

class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts: {account_number: balance}

    def create_account(self, account_number, initial_balance=0):
        """Create a new account with an initial balance."""
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with balance ${initial_balance:.2f}")

    def deposit(self, account_number, amount):
        """Deposit money into an account."""
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"${amount:.2f} deposited to account {account_number}.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        """Withdraw money from an account."""
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"${amount:.2f} withdrawn from account {account_number}.")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        """Check the balance of an account."""
        if account_number in self.accounts:
            balance = self.accounts[account_number]
            print(f"Account {account_number} balance: ${balance:.2f}")
            return balance
        else:
            print("Account not found.")
            return None

# Example usage
bank = Bank()
bank.create_account("12345", 1000)
bank.deposit("12345", 500)
bank.withdraw("12345", 200)
bank.check_balance("12345")

bank.withdraw("12345", 2000)  # Should show "Insufficient funds"
bank.check_balance("99999")  # Should show "Account not found"
