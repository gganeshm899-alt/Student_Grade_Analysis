# Student Grade Analysis System

## Description

The **Student Grade Analysis System** is a simple Python-based command-line application used to manage and analyze student marks.

The program stores student information, subject-wise marks, calculates total marks, percentage, grades, and pass/fail status. It also provides class-level and subject-level analysis.

This project is designed for beginners to demonstrate the use of:

- Python dictionaries
- Functions
- Loops
- Conditional statements
- Lists
- `sum()`, `max()`, and `min()`
- User input
- Basic data analysis

---

## Features

The project provides the following features:

1. **Display Student Report**
   - Search for a student using their Student ID.
   - Display name and subject-wise marks.
   - Calculate total marks.
   - Calculate percentage.
   - Display grade.
   - Display PASS/FAIL status.

2. **Class Analysis**
   - Display total number of students.
   - Calculate class average percentage.
   - Find the student with the highest percentage.
   - Find the student with the lowest percentage.

3. **Subject-wise Analysis**
   - Calculate average marks for each subject.
   - Find highest marks in each subject.
   - Find lowest marks in each subject.

4. **Grade Distribution**
   - Count the number of students receiving:
     - A+
     - A
     - B
     - C
     - D
     - F

5. **Display All Students**
   - Display the complete report of all students.

6. **Exit**
   - Safely exit the application.

---

## Technologies Used

- **Python 3**
- Command Line / Terminal
- No external libraries are required.

---

## Project Structure

```text
Student-Grade-Analysis/
│
├── student_grade_analysis.py
│
└── README.md
```

> Make sure that `README.md` is placed at the **root level of the repository**.

---

# Installation and Setup

## Step 1: Install Python

Download and install **Python 3** on your computer.

During installation on Windows, make sure to enable:

```text
Add Python to PATH
```

To check whether Python is installed correctly, open Command Prompt or Terminal and run:

```bash
python --version
```

You should see a Python 3 version, for example:

```text
Python 3.x.x
```

---

## Step 2: Clone the Repository

Open Command Prompt or Terminal and clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
```

Replace `<YOUR_REPOSITORY_URL>` with the URL of your GitHub repository.

For example:

```bash
git clone https://github.com/username/student-grade-analysis.git
```

Then move into the project directory:

```bash
cd student-grade-analysis
```

---

## Step 3: Check the Project Files

Make sure the repository contains:

```text
student_grade_analysis.py
README.md
```

The `README.md` file should be located directly inside the main project folder.

---

## Step 4: Environment Setup

This project does not require any external Python packages.

Therefore, there is **no dependency installation required**.

However, you can optionally create a virtual environment.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## Step 5: Install Dependencies

There are no external dependencies for this project.

The program uses only Python's built-in features.

Therefore, you do **not** need to run:

```bash
pip install ...
```

---

# Configuration

No separate configuration file is required.

The student records are stored directly inside the Python program using a dictionary.

Example:

```python
students = {
    "S101": {
        "name": "Ganesh M",
        "marks": {
            "Python": 95,
            "Mathematics": 92,
            "English": 94,
            "EVS": 95,
            "Physics": 90
        }
    }
}
```

To add or modify students, edit the `students` dictionary in the Python file.

Each student contains:

- Student ID
- Student name
- Python marks
- Mathematics marks
- English marks
- EVS marks
- Physics marks

---

# Running the Project

## Step 1: Open the Project Folder

Open Command Prompt or Terminal in the project directory.

Example:

```bash
cd student-grade-analysis
```

## Step 2: Run the Python Program

On Windows:

```bash
python student_grade_analysis.py
```

On macOS/Linux, you can use:

```bash
python3 student_grade_analysis.py
```

---

# Using the Application

After running the program, the following menu will appear:

```text
STUDENT GRADE ANALYSIS
1. Display Student Report
2. Class Analysis
3. Subject-wise Analysis
4. Grade Distribution
5. Display All Students
6. Exit

Enter your choice:
```

Enter a number from **1 to 6**.

---

## Option 1: Display Student Report

Enter:

```text
1
```

The program will ask for a Student ID:

```text
Enter Student ID:
```

For example:

```text
S101
```

The program displays:

```text
STUDENT REPORT
Student ID : S101
Name       : Ganesh M
Subject Marks:
Python         : 95
Mathematics    : 92
English        : 94
EVS            : 95
Physics        : 90
Total Marks: 466
Percentage : 93.2 %
Grade      : A+
Result     : PASS
```

---

## Option 2: Class Analysis

Enter:

```text
2
```

The program displays:

- Number of students
- Class average
- Highest percentage
- Highest-performing student
- Lowest percentage
- Lowest-performing student

---

## Option 3: Subject-wise Analysis

Enter:

```text
3
```

The program analyzes each subject and displays:

- Average marks
- Highest marks
- Lowest marks

Example:

```text
Subject: Python
Average Marks : ...
Highest Marks : ...
Lowest Marks  : ...
```

---

## Option 4: Grade Distribution

Enter:

```text
4
```

The program counts students according to their grades.

Example:

```text
GRADE DISTRIBUTION
Grade A+: 2 student(s)
Grade A: 2 student(s)
Grade B: 1 student(s)
Grade C: 1 student(s)
Grade D: 0 student(s)
Grade F: 0 student(s)
```

---

## Option 5: Display All Students

Enter:

```text
5
```

The program displays the complete report for every student stored in the system.

---

## Option 6: Exit

Enter:

```text
6
```

The program displays:

```text
Thank you
```

and exits.

---

# Grading System

The application uses the following grading criteria:

| Percentage | Grade |
|---|---|
| 90 or above | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

A student is considered **PASS** when all subject marks are at least **40**.

If any subject mark is below 40, the student is considered **FAIL**.

---

# Dependencies

This project has **no external dependencies**.

It requires only:

```text
Python 3.x
```

Python's built-in functions and data structures are sufficient to run the project.

---

# Troubleshooting

### Python command is not recognized

If you see an error such as:

```text
'python' is not recognized as an internal or external command
```

install Python and make sure **Add Python to PATH** was selected during installation.

You can also try:

```bash
py student_grade_analysis.py
```

on Windows.

### File not found

Make sure you are inside the project directory:

```bash
cd student-grade-analysis
```

Then run:

```bash
python student_grade_analysis.py
```

### Invalid choice

The menu accepts only numbers from:

```text
1
2
3
4
5
6
```

Enter a valid menu number when prompted.

---

# Future Improvements

The project can be extended in the future with:

- Add new students through user input
- Update student marks
- Delete student records
- Search students by name
- Save records to a file
- Read records from CSV/JSON files
- Generate printable student reports
- Add a graphical user interface
- Store data using a database

---

# Author

**Student Grade Analysis System**

This project was created as a Python programming project to demonstrate basic programming concepts and student data analysis.

---

# License

This project is intended for educational and academic purposes.
