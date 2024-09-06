def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():

    name = input("Hello! Please enter your name? \n")

    numbers = []
    for i in range(3):
        while True:
            try:
                number = int(input(f"Enter your favourite no. {i+1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Enter a valid integer.")

    print(f"\nNice to meet you, {name}!")

    even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

    print("\nHere are your favourite numbers with their even/odd decleration:")
    for num, status in even_odd_info:
        print(f"{num} is {status}.")

    squared_numbers = [(num, num**2) for num in numbers]

    print("\nHere are your favourite numbers and their squares:")
    for num, square in squared_numbers:
        print(f"The square of {num} is {square}.")

    total_sum = sum(numbers)
    print(f"\nThe sum of your favourite numbers is {total_sum}.")
    
    if is_prime(total_sum):
        print("The sum is a prime number! It's awesome!")
    else:
        print("The sum is not a prime number.")

if __name__ == "__main__":
    main()