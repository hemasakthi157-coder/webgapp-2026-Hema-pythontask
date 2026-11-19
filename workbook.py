
import csv
import os

def add_expense(amount, category):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category])

    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists("expenses.csv"):
        print("No expenses found!")
        return

    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)

        print("\n--- Expense Details ---")
        for row in reader:
            print("Amount:", row[0], "| Category:", row[1])

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = input("Amount: ")
        category = input("Category: ")
        add_expense(amount, category)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
