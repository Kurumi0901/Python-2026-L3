import os
import numpy as np
from domains.student import Student
from domains.course import Course
from domains.mark import Mark
from input import input_students, input_courses, input_marks, compress_files, load_data
from output import list_courses, list_students_sorted_by_gpa

def calculate_gpa(s_id, courses, marks):
    student_marks = []
    course_credits = []
    
    for m in marks:
        if m.student_id == s_id:
            for c in courses:
                if c.id == m.course_id:
                    student_marks.append(m.mark)
                    course_credits.append(c.credit)
                    break
                    
    if len(student_marks) == 0:
        return 0.0
    
    marks_array = np.array(student_marks)
    credits_array = np.array(course_credits)
    
    gpa = np.sum(marks_array * credits_array) / np.sum(credits_array)
    return round(float(gpa), 2)

def main():
    students = []
    courses = []
    marks = []

    loaded = load_data(students, courses, marks)

    if not loaded:
        print("\n--- NO PREVIOUS DATA FOUND. ENTERING NEW DATA ---")
        print("\n--- INPUT COURSES ---")
        input_courses(courses)

        print("\n--- INPUT STUDENTS ---")
        input_students(students)

        print("\n--- INPUT MARKS ---")
        input_marks(students, courses, marks)

        compress_files()
        print("\n[INFO] Data saved and compressed to 'students.dat'.")

    list_courses(courses)

    gpa_dict = {}
    for s in students:
        gpa_dict[s.id] = calculate_gpa(s.id, courses, marks)

    list_students_sorted_by_gpa(students, gpa_dict)

if __name__ == "__main__":
    main()