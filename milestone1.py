
# MIET Campus Library Borrowing and Fine Management System
# Milestone 1: Basic Data Handling

# Taking student and book details
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
book_title = input("Enter book title: ")

# Taking numerical inputs
days_kept = int(input("Enter days kept: "))
allowed_days = int(input("Enter allowed days: "))
fine_rate = int(input("Enter fine per day: "))

# Calculating overdue days and fine
overdue_days = max(0, days_kept - allowed_days)
fine = overdue_days * fine_rate

# Displaying library record
print("\n--- Library Record ---")
print("Student:", student_name.upper())
print("Roll Number:", roll_number)
print("Book:", book_title.title())
print("Days Kept:", days_kept)
print("Allowed Days:", allowed_days)
print("Overdue Days:", overdue_days)
print("Fine: Rs.", fine)
