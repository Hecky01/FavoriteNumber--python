#This is basic in out console app with random and if statement

import random

name1 = str(input("Whats your name?:"))

print(f"Hello {name1} it's nice to meet you!")

number1 = int(input("Whats your favorite number?:"))

random_number = random.randrange(1, 10)

if (number1 == random_number):
    print(f"so {name1} - your favorite number is {number1} - that's fantastic!!! {random_number} is also my favorite!")
else:
    print(f"so {name1} - your favorite number is {number1} - that's fantastic, mine is {random_number}")

