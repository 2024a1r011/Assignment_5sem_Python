
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
record_file = "library_records.txt"


def save_record(action, book_name):
    transaction_time = time.strftime("%d-%m-%Y %H:%M:%S")

    with open(record_file, "a") as file:
        file.write(
            f"{transaction_time} | {student_name} | "
            f"{action} | {book_name}\n"
        )

    print("Transaction record saved successfully.")


def display_records():
    print("\n===== SAVED LIBRARY RECORDS =====")

    try:
        with open(record_file, "r") as file:
            records = file.read()

            if records:
                print(records)
            else:
                print("No records found.")

    except FileNotFoundError:
        print("Record file does not exist yet.")


def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value

        except ValueError:
            print("Invalid input! Please enter a number.")


print("\n===== MIET LIBRARY MANAGEMENT SYSTEM =====")

while True:

    print("\n1. Borrow a book")
    print("2. Return a book")
    print("3. Calculate fine")
    print("4. View saved records")
    print("5. Display account summary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        if len(borrowed_books) >= 3:
            print("You cannot borrow more than 3 books.")

        else:
            book_name = input("Enter book name: ").strip()

            if is_available(catalogue, book_name):
                borrowed_books.append(book_name)
                catalogue[book_name] -= 1

                print("Successfully borrowed:", book_name)
                save_record("BORROWED", book_name)

            else:
                print("Book not found or currently unavailable.")

    elif choice == "2":

        book_name = input("Enter book name to return: ").strip()

        if book_name in borrowed_books:
            borrowed_books.remove(book_name)
            catalogue[book_name] += 1

            print("Successfully returned:", book_name)
            save_record("RETURNED", book_name)

        else:
            print("This book is not in your borrowed books list.")

    elif choice == "3":

        days_kept = get_integer("Enter days kept: ")
        allowed_days = get_integer("Enter allowed days: ")

        fine = calculate_fine(days_kept, allowed_days)

        print("Fine Amount: Rs.", fine)

    elif choice == "4":

        display_records()

    elif choice == "5":

        prepare_summary(student_name, borrowed_books)

    elif choice == "6":

        print("Thank you for using MIET Library!")
        break

    else:
        print("Invalid choice! Please select 1 to 6.")


print("\nFinal Catalogue:")

for book, copies in catalogue.items():
    print(book, ":", copies, "copies")
