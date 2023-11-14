#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.

# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return 'Error! Division by zero is not allowed.'
    else:
        return x / y


# To get inputs from user

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
operation = input('Enter operation (+, -, *, /): ')

# Performing selected operation

if operation == '+':
    print('Result: ', add(num1, num2))
elif operation == '-':
    print('Result: ', subtract(num1, num2))
elif operation == '*':
    print('Result: ', multiply(num1, num2))
elif operation == '/':
    print('Result: ', divide(num1, num2))
else:
    print('Invalid operation')