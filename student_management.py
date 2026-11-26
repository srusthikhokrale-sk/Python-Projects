import json

FILE_NAME = "students.json"


# Load student records from file
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


# Save student records to file
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Load existing records
students = load_students()


# 1. Add Student
def add_student():
    roll = input("Enter roll number: ")

    for student in students:
        if student["roll_no"] == roll:
            print("Roll number already exists!")
            return

    name = input("Enter student name: ")
    age = input("Enter age: ")

    if not age.isdigit() or int(age) <= 0:
        print("Invalid age!")
        return

    student = {
        "roll_no": roll,
        "name": name,
        "age": int(age)
    }

    students.append(student)
    save_students()

    print("Student added successfully!")


# 2. View Students
def view_students():
    if not students:
        print("No students found.")
    else:
        print("\n--- Student Records ---")

        for student in students:
            print("----------------------")
            print("Roll Number:", student["roll_no"])
            print("Name:", student["name"])
            print("Age:", student["age"])


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
            save_students()

            print("Student deleted successfully!")
            return

    print("Student not found.")


# 5. Update Student
def update_student():
    roll = input("Enter roll number to update: ")

    for student in students:
        if student["roll_no"] == roll:
            print("Current details:", student)

            new_name = input("Enter new name: ")
            new_age = input("Enter new age: ")

            if not new_age.isdigit() or int(new_age) <= 0:
                print("Invalid age!")
                return

            student["name"] = new_name
            student["age"] = int(new_age)

            save_students()

            print("Student updated successfully!")
            return

    print("Student not found.")


# Main Menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

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
        update_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")