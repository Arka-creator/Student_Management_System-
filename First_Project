#my first project with mysql database
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter MySQL password: "),
    database="student_db"
)

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
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)
    cursor.execute(query, values)
    db.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    for row in result:
        print(row)

def search_student():
    name = input("Enter name to search: ")
    query = "SELECT * FROM students WHERE name = %s"
    cursor.execute(query, (name,))
    result = cursor.fetchall()
    for row in result:
        print(row)

def delete_student():
    student_id = int(input("Enter ID to delete: "))
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    db.commit()
    print("Student deleted!")

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
        break
    else:
        print("Invalid choice!")