def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Math Error"

def calculator(n1, n2, operation):
    if operation == '1':
        return add(n1, n2)
    elif operation == '2':
        return subtract(n1, n2)
    elif operation == '3':
        return multiply(n1, n2)
    elif operation == '4':
        return divide(n1, n2)
    else:
        return "Invalid operation: Please select from 1, 2, 3, or 4."

def main():
    try:
        n1 = float(input("Enter the first number: \n"))
        n2 = float(input("Enter the second number: \n"))
        print("Select an operation:\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division ")
        operation = input("Enter the (1/2/3/4): \n")

        result = calculator(n1, n2, operation)
        print("Result:", result)

    except ValueError:
        print("Invalid Number: Please enter a valid number.")

main()