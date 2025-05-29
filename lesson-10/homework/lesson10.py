# Lesson 10 homework

# Homework 1: ToDo List Application

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"
        
    def mark_complete(self):
        self.status = "Complete"
        
    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}"

  # Step 2 ToDoList Class

class ToDoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added.\n")
        
    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"Task '{title}' marked as complete.\n")
                return
        print(f"No task found with title: {title}\n")
        
    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks in the list.\n")
            return
        print("All Tasks:")
        for task in self.tasks:
            print(task)
            print("-" * 40)
            found = True
        if not found:
            print("No incomplete tasks.\n")
        
        # Step 3: Main Program with CLI

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nToDo List Menu")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")
        
        choice = input(" Enter your choice (1-5): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (e.g., 2024-06-01): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            
        elif choice == "2":
            title = input("Enter the title of the task to mark as complete: ")
            todo_list.mark_task_complete(title)
            
        elif choice == "3":
            todo_list.list_all_tasks()
            
        elif choice == "4":
            todo_list.list_incomplete_tasks()
            
        elif choice == "5":
            print("Exiting ToDo List App. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            
            
if __name__ == "__main__":
    main()
        
         
        # Homework 2: Simple Blog System

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_title, new_content):
        self.title = new_title
        self.content = new_content

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}"

  # Step 2: Blog Class

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"Post '{post.title}' by {post.author} added.\n")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.\n")
            return
        print("All Blog Posts:")
        for post in self.posts:
            print(post)
            print("-" * 40)

    def list_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author == author_name:
                print(post)
                print("-" * 40)
                found = True
        if not found:
            print(f"No posts found by author '{author_name}'.\n")

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print(f"Post '{title}' deleted.\n")
                return
        print(f"Post with title '{title}' not found.\n")

    def edit_post(self, title):
        for post in self.posts:
            if post.title == title:
                new_title = input("Enter new title: ")
                new_content = input("Enter new content: ")
                post.edit(new_title, new_content)
                print(f"Post '{title}' updated.\n")
                return
        print(f"Post with title '{title}' not found.\n")

    def display_latest_posts(self, count=3):
        print(f"Latest {min(count, len(self.posts))} Posts:")
        for post in self.posts[-count:][::-1]:  # Display from latest to older
            print(post)
            print("-" * 40)


# Step 3: Main CLI Program

def main():
    blog = Blog()

    while True:
        print("\nBlog System Menu:")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(Post(title, content, author))

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name to search: ")
            blog.list_posts_by_author(author)

        elif choice == "4":
            title = input("Enter title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Enter title of the post to edit: ")
            blog.edit_post(title)

        elif choice == "6":
            try:
                count = int(input("How many recent posts to display? "))
            except ValueError:
                count = 3
            blog.display_latest_posts(count)

        elif choice == "7":
            print("Exiting Blog System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

      # Step 4: Run the program 
if __name__ == "__main__":
    main()

# Homework 3: Simple Banking System

# Step 1: account Class

class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient balance. Withdrawal denied.")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ${self.balance:.2f}")

  # Step 2: Bank Class

class Bank:
    def __init__(self):
        self.accounts = []

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def add_account(self, account_number, holder_name, balance=0.0):
        if self.find_account(account_number):
            print("Account with this number already exists.")
        else:
            account = Account(account_number, holder_name, balance)
            self.accounts.append(account)
            print("Account created successfully.\n")

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f"Balance: ${account.balance:.2f}")
        else:
            print("Account not found.")

    def deposit_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transfer_money(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Transferred ${amount:.2f} from {from_acc} to {to_acc}.")
            else:
                print("Transfer failed: Insufficient funds.")
        else:
            print("One or both accounts not found.")

    def display_account_details(self, account_number):
        account = self.find_account(account_number)
        if account:
            account.display_details()
        else:
            print("Account not found.")

# Step 3: Main CLI Program

def main():
    bank = Bank()

    while True:
        print("\nBanking System Menu")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            try:
                balance = float(input("Enter initial balance: "))
            except ValueError:
                balance = 0.0
            bank.add_account(acc_num, name, balance)

        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.check_balance(acc_num)

        elif choice == "3":
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to deposit: "))
                bank.deposit_money(acc_num, amount)
            except ValueError:
                print("Invalid amount.")

        elif choice == "4":
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw_money(acc_num, amount)
            except ValueError:
                print("Invalid amount.")

        elif choice == "5":
            from_acc = input("From Account Number: ")
            to_acc = input("To Account Number: ")
            try:
                amount = float(input("Enter amount to transfer: "))
                bank.transfer_money(from_acc, to_acc, amount)
            except ValueError:
                print("Invalid amount.")

        elif choice == "6":
            acc_num = input("Enter account number: ")
            bank.display_account_details(acc_num)

        elif choice == "7":
            print("Exiting Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
          
# Step 4: Running the Program

if __name__ == "__main__":
    main()
