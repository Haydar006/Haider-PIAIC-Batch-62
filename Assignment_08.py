books = []
users = []

# Defining function to add books to the library
def add_book(book_id, book_title, book_author, book_genre, book_status):
    book = {
        'Book ID' : book_id,    # Giving book a unique ID
        'Book Title' : book_title,   # Adding book title
        'Book Author' : book_author, # Adding book author
        'Book Genre' : book_genre,   # Adding book genre
        'Status' : book_status,
    }
    books.append(book)          # .append function to add more books to the library

# Defining User function to add users who borrowed book from the library
def add_user(user_id, user_name):
    user = {
        'User ID' : user_id,    # Giving user a unique user ID
        'User Name' : user_name # Adding users Name to the library
    }
    users.append(user)          # .append function to add more users to the library

# Defining a function to view all the books available at the library
def view_all_books():
    print('All Books:\n')
    for book in books:
        print(f"Book ID: {book['Book ID']}\nTitle: {book['Book Title']}\nAuthor: {book['Book Author']}\nGenre: {book['Book Genre']}\nStatus: {book['Status']}\n")
    print('\n')
    print('Choose from the following:\n')

# Defining a function to view all users accessing the library
def view_all_users():
    print('All Users:')
    for user in users:
        print(f"User ID: {user['User ID']}\nName: {user['User Name']}\n")
    print('Choose from the following:\n')

# defining searching books option to find books easily
def search_books(search_word):
    print("\nSearch Results:")
    found_books = [book for book in books if (search_word.lower() in book['Book Title'].lower() or
                                               search_word.lower() in book['Book Author'].lower() or
                                               search_word.lower() in book['Book Genre'].lower() or
                                               search_word.lower() in book['Status'].lower())]
    
    if found_books:
        for book in found_books:
            print(f"Book ID: {book['Book ID']}\nTitle: \"{book['Book Title']}\"\nAuthor: {book['Book Author']}\nGenre: {book['Book Genre']}\nStatus: ({book['Status']})\n")
        print('\nChoose from the following:\n')
    else:
        print("No books found.")

# defining a function to update the library if the users borrow a book
def borrow_book(user_id, book_id):
    user = next((user for user in users if user['User ID'] == int(user_id)), None)
    book = next((book for book in books if book['Book ID'] == int(book_id)), None)

    # Creating borrowed books list if it does not exists in user
    if user and 'Borrowed Books' not in user:
        user['Borrowed Books'] = []

    if user and book:
        if book['Status'] == 'Available':
            book['Status'] = 'Checked Out'
            user['Borrowed Books'].append(book)
            print(f"You have borrowed \"{book['Book Title']}\".")
            view_all_books()  # Updating the view_all_books function with the books status
        else:
            print(f"Sorry, the book \"{book['Book Title']}\" is currently checked out.")
    else:
        print("Invalid User ID or Book ID.")

# defining function to update the library with the books returned to the library by the user
def return_book(user_id, book_id):
    user = next((user for user in users if user['User ID'] == int(user_id)), None)
    book = next((book for book in books if book['Book ID'] == int(book_id)), None)

    if user and 'Borrowed Books' in user and book in user['Borrowed Books']:
        book['Status'] = 'Available'
        user['Borrowed Books'].remove(book)
        print(f"You have returned \"{book['Book Title']}\".")
        view_all_books()  # Updating the view_all_books function with the books status
    else:
        print("Invalid return request.")

# Defining the Menu to run the program
def menu():
    # Welcoming the user to library
    print('Welcome to the Library.')
    print('-----------------------')

    # loop to keep the program running until the user exits it
    while True:

    # Printing all the function available to view the library in the menu function
        print('1. View All Books')
        print('2. View All Users')
        print('3. Search for a book')
        print('4. Borrowing a Book')
        print('5. Returning a Book')
        print('6. Exit')
        print('\nEnter (1-6):')

    # setting up the menu with the functions
        user_input = input()
        if user_input == '1':
            view_all_books()
        elif user_input == '2':
            view_all_users()
        elif user_input == '3':
            search_word = input('Enter the Book Title, Author, Genre to search:')
            search_books(search_word)
        elif user_input == '4':
            user_id = input('Enter your user ID:\n')
            book_id = input('Enter the book ID:\n')
            borrow_book(user_id, book_id)
        elif user_input == '5':
            user_id = input('Enter your user ID:\n')
            book_id = input('Enter the Book ID:\n')
            return_book(user_id, book_id)
        elif user_input == '6':
            print('\n"Have a great day!"')
            print('-------------------')
            exit()
        else:
            print('Incorrect Input! Please Try Again.')

# adding books to the library
add_book(12345, "Mindset", "Carol Dweck", "Educational Psychology", "Available")
add_book(23456, "The 100: A Ranking of the Most Influential Persons in History", "Michael H. Hart", "Historical non-fiction, Biography, Ranking", "Available")
add_book(34567, "The Innovator's Dilemma", "Clayton M. Christensen", "Business, Technology", "Available")
add_book(45678, "Guinness Book of World Records", "Guinness family", "Reference, Almanac, and Trivia", "Available")
add_user(35201, "Haider")
add_user(35202, "Hussain")
add_user(35203, "Tabraiz")
add_user(35204, "Waleed")

# running the menu function to start the program
menu()