#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
def get_last_digit(number):
    return number % 10
last_digit = get_last_digit(number)
if last_digit > 5:
    print(f"last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"last digit of {number} is {last_digit} and is 0")
elif(last_digit < 6 and last_digit != 0):
    print(f"last digit of {number} is {last_digit} and is less than 6 and 0")
