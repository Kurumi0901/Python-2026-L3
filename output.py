def list_courses(courses):
    print("\n=== COURSE LIST ===")
    for c in courses:
        print(f"ID: {c.id} | Name: {c.name} | Credits: {c.credit}")

def list_students_sorted_by_gpa(students, gpa_dict):
    # Tạo danh sách tạm để sắp xếp
    gpa_list = []
    for s in students:
        gpa = gpa_dict.get(s.id, 0.0)
        gpa_list.append([s.id, s.name, gpa])
        
    # Sắp xếp GPA giảm dần
    gpa_list.sort(key=lambda x: x[2], reverse=True)
    
    print("\n=== STUDENT LIST SORTED BY GPA ===")
    for item in gpa_list:
        print(f"ID: {item[0]} | Name: {item[1]} | GPA: {item[2]}")