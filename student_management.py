students = []

# 1. Add Student
def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    age = input("Enter age: ")

    student = {
        "roll_no": roll,
        "name": name,
        "age": age
    }

    students.append(student)
    print("Student added successfully!")


# 2. View Students
def view_students():
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)


# 3. Search Student
def search_student():
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll:
            print("Student found:", student)
            return

    print("Student not found.")


# 4. Delete Student
def delete_student():
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Main Menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

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
        break
    else:
        print("Invalid choice!")