#my first project with mysql database
import mysql.connector
from getpass import getpass
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=getpass("Enter MySQL password: "),
        database="student_db"
    )
except mysql.connector.Error as err:
    print("Database connection failed:", err)
    exit()

cursor = db.cursor()
def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

def add_student():
    name = input("Enter name: ")
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Please enter a valid age.")
        return

    course = input("Enter course: ")
    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)
    cursor.execute(query, values)
    db.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        print("Students not found.")

def search_student():
    name = input("Enter name to search: ")
    query = "SELECT * FROM students WHERE name = %s"
    cursor.execute(query, (name,))
    result = cursor.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        print("Student not found.")

def delete_student():
    try:
        student_id = int(input("Enter ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    db.commit()
    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student ID not found.")

while True:
    menu()
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you!")
        cursor.close()
        db.close()
        break
    else:
        print("Invalid choice!")