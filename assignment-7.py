def prime_check(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 1  

    return True

def main():
    user = input("Hello! What is your name? \n")

    fav_numbers = []
    for n in range(3):
        while True:
            try:
                fav_number = int(input(f"Enter your favourite number {n+1}: "))
                fav_numbers.append(fav_number)
                break
            except ValueError:
                print("Invalid entry. Please provide a valid whole number.")

    print(f"\nPleasure meeting you, {user}!")

    parity_info = [(num, "even" if num % 2 == 0 else "odd") for num in fav_numbers]

    print("\nYour favourite numbers and their parity status:")
    for num, parity in parity_info:
        print(f"{num} is {parity}.")

    squared_values = [(num, num**2) for num in fav_numbers]

    print("\nHere are your favourite numbers and their squares:")
    for num, square in squared_values:
        print(f"{num} squared is {square}.")

    total = sum(fav_numbers)
    print(f"\nThe sum of your favourite numbers is {total}.")
    
    if prime_check(total):
        print("The sum of your favourite numbers is a prime number! Wow!")
    else:
        print("The sum of your favourite numbers is not a prime number.")

if __name__ == "__main__":
    main()
