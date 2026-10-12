import math
import numpy as np

# --- 1. DATA STRUCTURES ---
student_ID = []
student_name = []
student_class = []
DoB = []

# Store courses as: [course_ID, course_name, credit]
courses = [] 

# Store marks as: { (student_ID, course_ID): mark }
marks = {}

# --- 2. INPUT FUNCTIONS ---
def input_student():
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"\n--- Student {i + 1} ---")
        s_id = input("  Student ID: ")
        name = input("  Student Name: ")
        c_name = input("  Class: ")
        dob = input("  Date of Birth: ")

        student_ID.append(s_id)
        student_name.append(name)
        student_class.append(c_name)    
        DoB.append(dob)

def input_course():
    n = int(input("Enter number of courses: "))
    for i in range(n):
        print(f"\n--- Course {i + 1} ---")
        c_id = input("  Course ID: ")
        name = input("  Course Name: ")
        credit = int(input("  Credits: "))
        courses.append([c_id, name, credit])

def input_mark():
    c_id = input("\nEnter Course ID to input marks for: ")
    for s_id in student_ID:
        raw_mark = float(input(f"  Enter mark for student {s_id}: "))
        
        # Round down to 1 decimal place using math.floor
        rounded_mark = math.floor(raw_mark * 10) / 10
        
        marks[(s_id, c_id)] = rounded_mark

# --- 3. GPA CALCULATION USING NUMPY ---
def calculate_gpa(s_id):
    student_marks = []
    course_credits = []
    
    for c in courses:
        c_id = c[0]
        credit = c[2]
        
        if (s_id, c_id) in marks:
            student_marks.append(marks[(s_id, c_id)])
            course_credits.append(credit)
            
    if len(student_marks) == 0:
        return 0.0
    
    # Calculate weighted sum using numpy arrays
    marks_array = np.array(student_marks)
    credits_array = np.array(course_credits)
    
    gpa = np.sum(marks_array * credits_array) / np.sum(credits_array)
    return round(gpa, 2)

# --- 4. OUTPUT AND SORTING FUNCTIONS ---
def list_courses():
    print("\n=== COURSE LIST ===")
    for c in courses:
        print(f"ID: {c[0]} | Name: {c[1]} | Credits: {c[2]}")

def list_students_sorted_by_gpa():
    gpa_list = []
    for i in range(len(student_ID)):
        s_id = student_ID[i]
        s_name = student_name[i]
        gpa = calculate_gpa(s_id)
        gpa_list.append([s_id, s_name, gpa])
        
    # Sort students by GPA descending
    gpa_list.sort(key=lambda x: x[2], reverse=True)
    
    print("\n=== STUDENT LIST SORTED BY GPA ===")
    for item in gpa_list:
        print(f"ID: {item[0]} | Name: {item[1]} | GPA: {item[2]}")

# --- 5. MAIN EXECUTION ---
def main():
    input_course()
    input_student()
    
    list_courses()
    
    input_mark()
    list_students_sorted_by_gpa()

if __name__ == "__main__":
    main()