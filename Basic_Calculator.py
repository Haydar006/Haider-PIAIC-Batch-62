def calculator(n1, n2, operation):
    if operation == '+':
        return n1 + n2
    elif operation == '-':
        return n1 - n2
    elif operation == '*':
        return n1 * n2
    elif operation == '/':
        if n2 != 0: 
            return n1 / n2
        else:
            return "Math Error"
    else:
        return "Invalid operation"

n1 = float(input("Enter the first number: \n"))
n2 = float(input("Enter the second number: \n"))
operation = input("Enter the operation (+, -, *, /): \n")

result = calculator(n1, n2, operation)
print("Result:", result)
