
def calculate_fine(days_kept, allowed_days, rate=5):
    overdue_days = max(0, days_kept - allowed_days)
    fine = overdue_days * rate
    return fine


def is_available(catalogue, book_name):
    if book_name in catalogue and catalogue[book_name] > 0:
        return True
    else:
        return False


def prepare_summary(student_name, borrowed_books):
    print("\n===== LIBRARY TRANSACTION SUMMARY =====")
    print("Student Name:", student_name)

    if len(borrowed_books) > 0:
        print("Borrowed Books:")
        for book in borrowed_books:
            print("-", book)
    else:
        print("No books borrowed.")
