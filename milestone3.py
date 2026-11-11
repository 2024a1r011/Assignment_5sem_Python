
# MIET Campus Library Borrowing and Fine Management System
# Milestone 3: Object-Oriented Programming

class LibraryAccount:

    # Class variable
    library_name = "MIET Central Library"

    # Constructor
    def __init__(self, member_id, student_name):
        self.member_id = member_id
        self.student_name = student_name
        self.borrowed_books = []

    # Method to borrow a book
    def borrow_book(self, book_name):
        self.borrowed_books.append(book_name)
        print(book_name, "borrowed successfully.")

    # Method to return a book
    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            print(book_name, "returned successfully.")
        else:
            print(book_name, "is not in the borrowed books list.")

    # Method to display account details
    def display_account(self):
        print("\n--- Library Account Details ---")
        print("Library:", LibraryAccount.library_name)
        print("Member ID:", self.member_id)
        print("Student Name:", self.student_name)
        print("Borrowed Books:", self.borrowed_books)

    # Special method to represent the object as a string
    def __str__(self):
        return f"{self.student_name} ({self.member_id})"


# Creating two LibraryAccount objects
account1 = LibraryAccount("2024A1R011", "Vishavjeet")
account2 = LibraryAccount("2024A1R012", "Rahul")

# Borrowing books
account1.borrow_book("Python Basics")
account1.borrow_book("Data Structures")

account2.borrow_book("Computer Networks")

# Returning a book
account1.return_book("Data Structures")

# Displaying account information
account1.display_account()
account2.display_account()

# Displaying objects using __str__()
print("\n--- Object Representation ---")
print(account1)
print(account2)
