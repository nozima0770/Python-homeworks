#1
from datetime import datetime
name = input("Enter your name:")
birth_year = int(input("Enter your year of birth:"))
current_year = datetime.now().year
age = current_year - birth_year
print(f"Hello, {name}! You are {age} years old.")

#2
from collections import Counter

txt= 'LMaasleitbtui'
txt[0::2]
#3
from collections import Counter

txt= 'MsaatmiazD'
txt[0::2]

#4

txt = "I'am John. I am from London"
residence = txt.split('from')[-1].strip()
print("Residence area:", residence)

#5
a=input("Enter text:")
print(a[::-1])

#6
text=input("Enter a string:")
vowels = 'aeiouAEIOU'
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count +=1
 
print("Number of vowels:", vowel_count)  

#7
numbers = input("5 22 3 4 7 ")
number_list = [int(num) for num in numbers.split()]
max_value = max(number_list)
("The maximum value is:", max_value)

#8
word = input("Enter a word:")
reversed_word = word[::-1]
if word == reversed_word:
    print("Yes. it's a palindrome!")
else:
    print("No, it's not a palindrome.")

#9
e = input("Enter email: ")
a = e.index('.')
print[a+1:]

#10
import random
import string

password_length = int(input("Enter password length:"))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(password_length))

print("Generated password:", password)



#9
e = input("Enter email: ")
a = e.index('.')
e[a+1:]
