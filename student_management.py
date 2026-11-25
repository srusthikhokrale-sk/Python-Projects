students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    branch = input("Enter branch: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "branch": branch
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print(student)
def search_student():
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll:
            print("Student Found!")
            print(student)
            return

    print("Student not found.")
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")