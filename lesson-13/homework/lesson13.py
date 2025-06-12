# Lesson 13 Homework
# task 1: Age Calculator 

from datetime import datetime

def calculate_age():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()
    
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day
    
    if days < 0:
        months -= 1
        days += 30
    if months < 0:
        years -= 1
        months += 12
        
    print(f"You are {years} years, {months} months, and {days} days old.")

calculate_age()

# task 2: Days Until Next Birthday

def days_until_birthday():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()
    next_birthday = birthdate.replace(year = today.year)
    
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
        
    delta = next_birthday - today
    print(f"Days until next birthday: {delta.days}")
    
days_until_birthday()

# task 3: Meeting Scheduler

from datetime import timedelta

def meeting_scheduler():
    now_str = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
    duration_hr = int(input("Enter meeting duration hours: "))
    duration_min = int(input("Enter meeting duration minutes: "))
    
    start_time = datetime.strptime(now_str, "%Y-%m-%d %H:%M")
    end_time = start_time + timedelta(hours=duration_hr, minutes=duration_min)
    
    print(f"Meeting will end at: {end_time}")
    
meeting_scheduler()

# Task 4: Timezone Converter


from datetime import datetime
from zoneinfo import ZoneInfo

def timezone_converter():
    date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_zone = input("Enter your timezone (e.g., 'Asia/Tashkent'): ")
    to_zone = input("Enter target timezone (e.g., 'America/New_York'): ")
    
    try:
        # Parse the date string
        naive_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        
        # Attach the source timezone
        source_dt = naive_dt.replace(tzinfo=ZoneInfo(from_zone))
        
        # Convert to target timezone
        target_dt = source_dt.astimezone(ZoneInfo(to_zone))
        
        print(f"\n Original ({from_zone}): {source_dt}")
        print(f"Converted ({to_zone}): {target_dt}")
        
    except Exception as e:
        print("Error during timezone conversion:", e)
        
        
timezone_converter()
        
# Task 5: Countdown Timer

import time

def countdown_timer():
    target_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
    target = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")
    
    while True:
        now = datetime.now()
        remaining = target - now
        if remaining.total_seconds() <=0:
            print("Time's up!")
            break
        print(f"Time remaining: {remaining}", end="\r")
        time.sleep(1)
        
countdown_timer()


# Task 6: Email Validator

import re

def email_validator():
    email = input("Enter email address: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(pattern, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")
        
email_validator()

# Task 7: Phone Number Formatter

def format_phone_number():
    raw = input("Enter a 10-digit phone number: ")
    if len(raw) == 10 and raw.isdigit():
        formatted = f"({raw[0:3]}) {raw[3:6]}-{raw[6:10]}"
        print("Formatted number:", formatted)
    else:
        print("Invalid input. Please enter exactly 10 digits.")
        
format_phone_number()

# Task 8: Password Strength Checker

import re 


def check_password_strength():
    pwd = input("Enter your password: ")
    if (len(pwd) >= 9 and
        re.search(r"[A-Z]", pwd) and
        re.search(r"[a-z]", pwd) and
        re.search(r"[0-9]", pwd)):
        print("Strong password.")
    else:
        print("Weak password. Use at least 8 characters, mix upper/lowercase and numbers.")
        
check_password_strength()

# Task 9: Word Finder

def word_finder():
    text = input("Enter a text: ")
    word = input("Enter the word to search: ")
    matches = [i for i in range(len(text)) if text.startswith(word, i)]
    print(f"Found '{word}' at positions:", matches)
    
word_finder()

# Task 10: Date Extractor

import re

def date_extractor():
    text = input("Enter text: ")
    pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    dates = re.findall(pattern, text)
    print("Dates found:", dates)

date_extractor()

