"""
day06_functions.py
Learning functions in Python
Author: Guillermo Justiniano Poehlmann
Date: 2026-01-24
"""
# Exercise 1: Function 
from unittest import result


def print_My_Goal ():
    print("My goal is to be a Millioneare before my 30s")
print_My_Goal()

# Exercise 2: Function with parameters
def greet_country(country):
    print(f"\nI will be six moths in {country} persuing my dreams.")
greet_country("Brazil")
greet_country("Indonesia")
greet_country("USA")
greet_country("China")
greet_country("Mexico")

# Exercise 3: Function with multiple parameters

def calculate_income(income_hour, income_weekly):
    monthly_from_hour = income_hour * 40 * 4
    monthly_from_week = income_weekly * 4
    annual_from_hour = income_hour * 40 * 4 * 12
    annual_from_week = income_weekly * 52
    print(f"\n My monthly income based on hourly pay is: ${monthly_from_hour}")
    print(f"\n My monthly income based on weekly pay is: ${monthly_from_week}")
    print(f"\n My annual income based on hourly pay is: ${annual_from_hour}")
    print(f"\n My annual income based on weekly pay is: ${annual_from_week}")
    
hourly_income = 1000
weekly_income = 40000
calculate_income(hourly_income, weekly_income)

# Exercise 4: Function with return value
def add_and_return(a, b):
    return a + b
result1 = add_and_return(15, 25)
print(f"\n The result of adding 15 and 25 is: {result1}")


def multiply_and_return(a, b):
    return a * b
result2 = multiply_and_return(15, 25)
print(f"\n The result of multiplying 15 and 25 is: {result2}")


returned_sum = add_and_return(result1, result2)
print(f"\n The sum of {result1} and {result2} is: {returned_sum}")

# Exercise 5: Average function
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return f"\n The average of the list {numbers} is: {average:.2f}"
numbers = [10, 20, 30, 40, 50]
print(calculate_average(numbers))

# Exercise 6: Temperature conversion function
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temp_1 = fahrenheit_to_celsius(100)
print(f"100°F = {temp_1:.2f}°C")

temp_2 = fahrenheit_to_celsius(32)
print(f"32°F = {temp_2:.2f}°C")

temp_3 = fahrenheit_to_celsius(60)
print(f"60°F = {temp_3:.2f}°C")

# Exercise 7: Prime number checker function
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
num = 26
if is_prime(num):
    print(f"\n {num} is a prime number.")
else:
    print(f"\n {num} is not a prime number.")