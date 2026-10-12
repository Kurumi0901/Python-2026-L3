import os
import gzip
import math
from domains.student import Student
from domains.course import Course
from domains.mark import Mark

def input_students(students):
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"\n--- Student {i + 1} ---")
        s_id = input("  Student ID: ")
        name = input("  Student Name: ")
        dob = input("  Date of Birth: ")
        students.append(Student(s_id, name, dob))
    save_students(students)

def input_courses(courses):
    n = int(input("Enter number of courses: "))
    for i in range(n):
        print(f"\n--- Course {i + 1} ---")
        c_id = input("  Course ID: ")
        name = input("  Course Name: ")
        credit = int(input("  Credits: "))
        courses.append(Course(c_id, name, credit))
    save_courses(courses)

def input_marks(students, courses, marks):
    while True:
        c_id = input("\nEnter Course ID to input marks for: ")
        
        course_exists = any(c.id == c_id for c in courses)
        if not course_exists:
            print(f"Course ID '{c_id}' not found! Please try again.")
            continue

        for s in students:
            raw_mark = float(input(f"  Enter mark for student {s.name} ({s.id}): "))
            rounded_mark = math.floor(raw_mark * 10) / 10
            marks.append(Mark(c_id, s.id, rounded_mark))
        
        cont = input("\nDo you want to input marks for another course? (y/n): ").strip().lower()
        if cont != 'y':
            break

    save_marks(marks)

def save_students(students):
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.id},{s.name},{s.dob}\n")

def save_courses(courses):
    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.id},{c.name},{c.credit}\n")

def save_marks(marks):
    with open("marks.txt", "w", encoding="utf-8") as f:
        for m in marks:
            f.write(f"{m.course_id},{m.student_id},{m.mark}\n")

def compress_files():
    files_to_compress = ["students.txt", "courses.txt", "marks.txt"]
    with open("students.dat", "wb") as f_out:
        for fname in files_to_compress:
            if os.path.exists(fname):
                with open(fname, "rb") as f_in:
                    f_out.write(f"=== {fname} ===\n".encode("utf-8"))
                    f_out.write(f_in.read())
                    f_out.write(b"\n")


def load_data(students, courses, marks):
    if not os.path.exists("students.dat"):
        return False

    print("\n[INFO] Found 'students.dat'. Loading existing data...")
    
    current_file = None
    with open("students.dat", "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("==="):
                if "students.txt" in line:
                    current_file = "students"
                elif "courses.txt" in line:
                    current_file = "courses"
                elif "marks.txt" in line:
                    current_file = "marks"
                continue

            parts = line.split(",")
            if current_file == "students" and len(parts) == 3:
                students.append(Student(parts[0], parts[1], parts[2]))
            elif current_file == "courses" and len(parts) == 3:
                courses.append(Course(parts[0], parts[1], int(parts[2])))
            elif current_file == "marks" and len(parts) == 3:
                marks.append(Mark(parts[0], parts[1], float(parts[2])))
                
    return True
