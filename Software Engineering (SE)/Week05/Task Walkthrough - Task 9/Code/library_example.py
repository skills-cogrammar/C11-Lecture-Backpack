'''
You are managing a small library and want to keep track of the books 
available. Every time a user wants to borrow a book, you need to check
if the book exists and if there are any copies left. Use a dictionary
to store this information.
'''

'''
Create a Book class and initialise a constructor that takes in 3
arguments for the book title, author, and number of copies. Inside
the contructor, initialise the necessary instance variables. Also 
add a copy_in_library method for the Book class that checks if 
there is at least one copy of the book available.
'''

class Book: # defining a Book class to be the blueprint
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies


    # Method to check if copy is available
    def copy_in_library(self):
        # Return True if there is at least 1 copy, False otherwise
        return self.copies > 0 

'''
Initialise an empty variable called library of type dictionary
to store and access book objects:
   - the key is the title of the book.
   - the value is an instance of the Book class.
'''
library = {}

'''
Create the following functions:

 1. populate_library() - a function that adds 3 books to the library
    dictionary. Just as in the task, at program start-up, this 
    function should be used to populate your library with three sample 
    book objects for further use in your program. This function does 
    not need to be included as a menu option for the user.

 2. list_books() - a function that loops through the library 
    dictionary and prints each book's title, author, and how many
    copies are available.

 3. list_available_books() - a function that lists only books that
    have at least one copy available.

 4. borrow_a_book() - the user enters the title of the book they want 
    to borrow, and the function checks if the book is in the library 
    and if there are copies available.
'''
def populate_library():
    library["Atomic Habits"] = Book("Atomic Habits","James Clear", 2)
    library["Brave New World"] = Book("Brave New World", "Aldous Huxley", 1)
    library["The Twilight Saga"] = Book("The Twilight Saga", "Stephenie Meyer", 0)


def list_books():
    for title, book in library.items():
        print(f'''Title: {title}, Author: {book.author}, 
        Number of copies available: {book.copies}''')


def list_available_books():
    for title, book in library.items(): # title is the key & book is the object value
        if book.copy_in_library():
            print(f'''Title: {title}, Author: {book.author}, 
            Number of copies available: {book.copies}''')


def borrow_a_book(title):
    # check if book exists AND if there are any copies available to borrow
    if title in library and library[title].copy_in_library():
        library[title].copies -= 1
        print(f"You have borrowed {title}.")
    else:
        print("That book is not available.")


#==================   Main Program    ==================
# Create a simple main menu that gives the user options to list books, 
# view available books, borrow a book, or quit the application.

# We need to get some books in our library
populate_library()

choice = '0'
while choice != '4':
    print('What would you like to do?')
    print('1. List all the books')
    print('2. List available books')
    print('3. Borrow a Book')
    print('4. Quit')

    choice = input("Enter the number of your choice option: ")

    # choice is 1 and function to call is list_books
    if choice == '1':
        list_books()
    elif choice == '2':
        list_available_books()
    elif choice == '3':
        title = input("Enter the title of the book you would like to borrow: ")
        borrow_a_book(title)
    elif choice == '4':
        print('Goodbye!')
    else:
        print("Choice invalid.")
