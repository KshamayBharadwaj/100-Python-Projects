# Simple Calculator in Python

def add(x, y):
    return x + y  # Function to add two numbers

def subtract(x, y):
    return x - y  # Function to subtract two numbers

def multiply(x, y):
    return x * y  # Function to multiply two numbers

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero"  # Function to divide two numbers, with zero check

# Displaying menu options
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Taking user input
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing the selected operation
if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")  # Handling invalid choices
