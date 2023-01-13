#Password Generator
import string
import random

letters_num = int(input("How many letters would you like in your password? "))
symbols_num = int(input("How many symbols would you like? "))
numbers_num = int(input("How many numbers would you like? "))

letters = string.ascii_letters
symbols = string.punctuation
numbers = string.digits

r_letters = "".join(random.choice(letters) for i in range(letters_num))
r_symbols = "".join(random.choice(symbols) for i in range(symbols_num))
r_numbers = "".join(random.choice(numbers) for i in range(numbers_num))

password_1 = r_letters + r_symbols + r_numbers

print(password_1)

password_2 = "".join(random.sample(password_1, len(password_1)))

print(password_2)
