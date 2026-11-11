
import time

from library_utils import calculate_fine
from library_utils import is_available
from library_utils import prepare_summary


catalogue = {
    "Python Basics": 2,
    "Data Structures": 1,
    "Computer Networks": 2,
    "Operating Systems": 0
}

student_name = input("Enter student name: ")

borrowed_books = []

print("\n===== MIET LIBRARY CATALOGUE =====")

for book, copies in catalogue.items():
    print(book, ":", copies, "copies")


while len(borrowed_books) < 3:

    book_name = input("\nEnter book name (or DONE to stop): ").strip()

    if book_name.upper() == "DONE":
        break

    if is_available(catalogue, book_name):

        borrowed_books.append(book_name)
        catalogue[book_name] -= 1

        print("Successfully borrowed:", book_name)

    else:
        print("Book not found or currently unavailable.")


prepare_summary(student_name, borrowed_books)


print("\n===== FINE CALCULATION =====")

days_kept = int(input("Enter days kept: "))
allowed_days = int(input("Enter allowed days: "))

fine = calculate_fine(days_kept, allowed_days)

print("Fine Amount: Rs.", fine)


print("\n===== UPDATED CATALOGUE =====")

for book, copies in catalogue.items():
    print(book, ":", copies, "copies")


transaction_time = time.strftime("%d-%m-%Y %H:%M:%S")

print("\nTransaction Time:", transaction_time)
print("Library transaction completed.")
