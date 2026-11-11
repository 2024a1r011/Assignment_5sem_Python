
# MIET Campus Library Borrowing and Fine Management System
# Milestone 2: Book Catalogue and Borrowing Management

# Creating the book catalogue
catalogue = {
    "Python Basics": 2,
    "Data Structures": 1,
    "Computer Networks": 2,
    "Operating Systems": 0
}

# Creating an empty list for borrowed books
borrowed_books = []

# Successful borrowing counter
count = 0

print("===== MIET LIBRARY CATALOGUE =====")

# Displaying available books
for book, copies in catalogue.items():
    print(book, ":", copies, "copies")

print("\nYou can borrow a maximum of 3 books.")
print("Enter DONE to stop borrowing.\n")

# Borrowing process
while count < 3:

    book = input("Enter book name: ").strip()

    # Checking the exit condition
    if book.upper() == "DONE":
        break

    # Checking whether the book exists
    if book in catalogue:

        # Checking whether copies are available
        if catalogue[book] > 0:

            borrowed_books.append(book)
            catalogue[book] -= 1
            count += 1

            print("Successfully borrowed:", book)
            print("Remaining copies:", catalogue[book])

        else:
            print("Sorry, this book is currently unavailable.")

    else:
        print("Book not found in the catalogue.")

# Displaying final borrowing information
print("\n===== BORROWING SUMMARY =====")

if len(borrowed_books) > 0:
    print("Borrowed books:")

    for book in borrowed_books:
        print("-", book)
else:
    print("No books were borrowed.")

print("\n===== UPDATED CATALOGUE =====")

for book, copies in catalogue.items():
    print(book, ":", copies, "copies")

print("\nTotal successful borrowings:", count)
print("Thank you for using MIET Library!")
