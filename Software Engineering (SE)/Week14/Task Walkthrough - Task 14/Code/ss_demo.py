'''
Example for Task14.1

Using the Book class, do the following:

1. Populate a list with elements of the Book class
2. Append a book to the list and swap the positions of items in the list
3. Extend one list that contains objects of the Book class with more Book objects 
   from another list
4. Sort according to number of copies available, using the key parameter and creating 
   a lambda function to access copy numbers
5. Find a book within the list and using the enumerate function to retrieve the 
   position of this book after ranking according to number of copies
'''


class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def copy_in_library(self):
        """Checks if at least one copy is available."""
        return self.copies > 0 

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"'{self.title}' by {self.author} ({self.copies} copies available)"


# 1. Populate a list with elements of the Book class
library = [
    Book("1984", "George Orwell", 4),
    Book("Long Walk to Freedom", "Nelson Mandela", 15),
    Book("The Power of Mental Discipline", "Alec Zeit", 24)
]

print("📚 Initial Library Collection:")
for book in library:
    print(f"  - {book}")

# 2. Append a book to the list and swap the positions of items in the list
new_book = Book("Alice in Wonderland", "Lewis Carroll", 0)
library.append(new_book)

print("\n📖 Added a new book:")
print(f"  - {library[len(library) - 1]}")

# Swap the first and last book
library[0], library[len(library) - 1] = library[len(library) - 1], library[0]

print("\n🔄 Swapped the first and last book in the list.")
print("📚 Updated Library Collection:")
for book in library:
    print(f"  - {book}")

# 3. Extend the list with more books
more_books = [Book("The Room on the Roof", "Ruskin Bond", 37)]
library.extend(more_books)

print("\n📚 Added more books:")
for book in more_books:
    print(f"  - {book}")

# 4. Sort by number of copies available
library.sort(key=lambda book: book.copies)

print("\n📊 Library sorted by the number of copies available:")
for book in library:
    print(f"  - {book}")

# 5. Find a specific book and display its position
book_to_find = "The Room on the Roof"

print("\n🔍 Searching for the book position after sorting...")
for index, book in enumerate(library):
    if book.title == book_to_find:
        print(f"✅ The book '{book_to_find}' is now at position {index + 1} in the sorted list.")
        break
