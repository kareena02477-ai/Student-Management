
import database

database.create_table()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        email = input("Enter Email: ")

        database.add_student(name, age, course, email)

    elif choice == "2":
        database.view_students()

    elif choice == "3":
        student_id = int(input("Enter Student ID: "))
        database.search_student(student_id)

    elif choice == "4":
        student_id = int(input("Enter Student ID: "))
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ")
        email = input("Enter New Email: ")

        database.update_student(
            student_id, name, age, course, email
        )

    elif choice == "5":
        student_id = int(input("Enter Student ID: "))
        database.delete_student(student_id)

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
