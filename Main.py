students = {"S101": {"name": "Ganesh M","marks": {"Python": 95,"Mathematics": 92,"English": 94,"EVS": 95,"Physics": 90}},
    "S102": {"name": "Yash Ghodke","marks": {"Python": 95,"Mathematics": 91,"English": 93,"EVS": 88,"Physics": 96}},
    "S103": {"name": "Omkar","marks": {"Python": 87,"Mathematics": 84,"English": 82,"EVS": 89,"Physics": 84}},
    "S104": {"name": "Abhijeet","marks": {"Python":85 ,"Mathematics": 90,"English": 85,"EVS": 92,"Physics": 89}},
    "S105": {"name": "Priya ","marks": {"Python":45 ,"Mathematics":52 ,"English": 48,"EVS": 55,"Physics":50 }}, 
    "S106": {"name": "Ananya","marks": {"Python":65 ,"Mathematics":72 ,"English": 65,"EVS": 57,"Physics":73 }}}
def grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"
def result(marks):
    total = sum(marks.values())
    subjects = len(marks)
    percentage = total / subjects
    grade = grade(percentage)
    if all(mark >= 40 for mark in marks.values()):
        status = "PASS"
    else:
        status = "FAIL"
    return total, percentage, grade, status
def student(id):
    if id not in students:
        print("not found")
        return
    student = students[id]
    total, percentage, grade, status = result( student["marks"])
    print("STUDENT REPORT")
    print("Student ID :", id)
    print("Name       :", student["name"])
    print("Subject Marks:")
    for subject, mark in student["marks"].items():
        print(f"{subject:<15}: {mark}")
    print("Total Marks:", total)
    print("Percentage :", percentage, "%")
    print("Grade      :", grade)
    print("Result     :", status)
def class_analysis():
    percentages = []
    highest = None
    lowest = None
    highestp = -1
    lowestp = 101
    for id, student in students.items():
        total, percentage, grade, status = result(
            student["marks"]
        )
        percentages.append(percentage)
        if percentage > highestp:
            highestp = percentage
            highest = student["name"]
        if percentage < lowestp:
            lowestp = percentage
            lowest = student["name"]
    class_average = sum(percentages) / len(percentages)
    print("          CLASS ANALYSIS")
    print("Number of Students :", len(students))
    print("Class Average      :", round(class_average, 2), "%")
    print("Highest Percentage :", (highestp), "%")
    print("Highest Student    :", highest)
    print("Lowest Percentage  :", (lowestp), "%")
    print("Lowest Student     :", lowest)
def analysis():
    print(" SUBJECT-WISE ANALYSIS")
    subjects = list(next(iter(students.values()))["marks"].keys())
    for subject in subjects:
        marks = []
        for student in students.values():
            marks.append(student["marks"][subject])
        average = sum(marks) / len(marks)
        highest = max(marks)
        lowest = min(marks)
        print("Subject:", subject)
        print("Average Marks :", round(average, 2))
        print("Highest Marks :", highest)
        print("Lowest Marks  :", lowest)
def distribution():
    grades = {"A+": 0,"A": 0,"B": 0,"C": 0,"D": 0,"F": 0}
    for student in students.values():
        total, percentage, grade, status = result(student["marks"])
        grades[grade] += 1
    print("GRADE DISTRIBUTION")
    for grade, count in grades.items():
        print(f"Grade {grade}: {count} student(s)")
def main():
    while True:
        print("STUDENT GRADE ANALYSIS")
        print("1. Display Student Report")
        print("2. Class Analysis")
        print("3. Subject-wise Analysis")
        print("4. Grade Distribution")
        print("5. Display All Students")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            id = input("Enter Student ID: ")
            student(id)
        elif choice == 2:
            class_analysis()
        elif choice == 3:
            analysis()
        elif choice == 4:
            distribution()
        elif choice == 5:
            for id in students:
                student(id)
        elif choice == 6:
            print("Thank you ")
            break
        else:
            print("Invalid choice")
main()
