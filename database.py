
import sqlite3

def connect_db():
    return sqlite3.connect("students.db")


def create_table():
    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT,
            email TEXT
        )
    """)

    con.commit()
    con.close()


def add_student(name, age, course, email):
    con = connect_db()
    cur = con.cursor()

    cur.execute(
        "INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
        (name, age, course, email)
    )

    con.commit()
    con.close()
    print("Student added successfully!")


def view_students():
    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT * FROM students")
    records = cur.fetchall()

    print("\n----- Student Records -----")

    if not records:
        print("No students found.")
    else:
        for student in records:
            print(student)

    con.close()


def search_student(student_id):
    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    record = cur.fetchone()

    if record:
        print("\nStudent Found:", record)
    else:
        print("Student not found.")

    con.close()


def update_student(student_id, name, age, course, email):
    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        UPDATE students
        SET name = ?, age = ?, course = ?, email = ?
        WHERE id = ?
    """, (name, age, course, email, student_id))

    con.commit()

    if cur.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student not found.")

    con.close()


def delete_student(student_id):
    con = connect_db()
    cur = con.cursor()

    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))

    con.commit()

    if cur.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")

    con.close()
