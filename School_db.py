import sqlite3

def connect_db():
    return sqlite3.connect('school.db')

def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
        """)
        conn.commit()

def add_student(name, age, grade):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO students (name, age, grade) VALUES (?, ?, ?)
        """, (name, age, grade))
        conn.commit()

def get_students():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

def update_student(student_id, name, age, grade):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?
        """, (name, age, grade, student_id))
        conn.commit()

def delete_student(student_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()

def main():
    create_table()
    print("School Database Management System")
    while True:
        print("\n1. Add Student")
        print("\n2. View Students")
        print("\n3. Update Student")
        print("\n4. Delete Student")
        print("\n5. Exit")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            add_student(name, age, grade)
        elif choice == '2':
            students = get_students()
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            grade = input("Enter new grade: ")
            update_student(student_id, name, age, grade)
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
