import string
import random

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)



print("Welcome to Password Generator!")
nr_letters = int(input(f"How many letters would you like?: \n"))
nr_numbers = int(input(f"How many numbers would you like?: \n"))
nr_symbols = int(input(f"How many symbols would you like?: \n"))

# Easy level
"""
password = '' 
for char in range(0,nr_letters):
    password += random.choice(letters)

for char in range(0,nr_symbols):
    password += random.choice(symbols)
    
for char in range(0,nr_numbers):
    password += random.choice(numbers) 
"""
            
# Hard Lever
password_list = []
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
    
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
password = ""
for char in password_list:
    password+=char
    
print(password_list)
print(f"Your password is: {password}")