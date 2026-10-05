
# check Even Number
def is_even(number):
    return number % 2 == 0

# Check Prime Number
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Check Palindrome
def is_palindrome(value):
    value = str(value)
    return value == value[::-1]

# Calculate Sum using *args
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


# Calculate Average
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


# Find Factors
def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


# Calculate Grade
def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks"
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


# Calculate Total

def calculate_total(price, quantity=1):
    if price < 0 or quantity < 0:
        return "Invalid input"
    return price * quantity


# Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Find Maximum
def find_maximum(numbers):
    if len(numbers) == 0:
        return None
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


# Find Minimum
def find_minimum(numbers):
    if len(numbers) == 0:
        return None
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum


#Build Profile using **kwargs
def build_profile(**details):
    return details