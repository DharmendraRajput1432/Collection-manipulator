# 🎓 Student Data Organizer

A simple **Python Console Application** that helps manage student records using Python collections such as **List, Dictionary, Set, and Tuple**.

This project is designed for beginners to practice CRUD (Create, Read, Update, Delete) operations and understand how different Python collection data types work together.

---

## 📌 Features

- ➕ Add Student
- 📋 Display All Students
- ✏️ Update Student Details
- ❌ Delete Student
- 📚 Display Subjects Offered
- 🚪 Exit Program

---

## 🛠 Technologies Used

- Python 3
- Lists
- Dictionaries
- Sets
- Tuples
- Loops
- Conditional Statements
- User Input

---

## 📂 Project Structure

```
Student_Data_Organizer/
│
├── student_data_organizer.py
└── README.md
```

---

## 📖 Student Information Stored

Each student record contains:

- Student ID
- Name
- Age
- Grade
- Date of Birth
- Subjects

Example:

```python
{
    "tup_id": "101",
    "name": "Rahul",
    "age": 20,
    "grade": "A",
    "tup_dob": "2005-06-15",
    "subjects": {"Python", "DBMS", "Java"}
}
```

---

## 📋 Menu

```
Welcome to the Student Data Organizer!

1. Add Student
2. Display All Students
3. Update Student
4. Delete Student
5. Display Subjects Offered
6. Exit
```

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/yourusername/student-data-organizer.git
```

### Navigate to the project folder

```bash
cd student-data-organizer
```

### Run the program

```bash
python student_data_organizer.py
```

or

```bash
python3 student_data_organizer.py
```

---

## 📚 Concepts Used

This project demonstrates:

- List Operations
- Dictionary Operations
- Set Operations
- Tuple Usage
- CRUD Operations
- Loops
- Functions (if added later)
- Conditional Statements
- User Input Handling

---

## 🔍 Collections Used

### List

Stores all student records.

```python
students = []
```

---

### Dictionary

Stores individual student information.

```python
student = {
    "tup_id": student_id,
    "name": name,
    "age": age,
    "grade": grade,
    "tup_dob": dob,
    "subjects": subject_set
}
```

---

### Set

Stores unique subjects.

```python
subject_set = set(subjects)
```

---

### Tuple

Used for immutable student information (ID and Date of Birth).

---

## 📸 Sample Output

```
Enter Student Details

Student ID : 101
Name : Rahul
Age : 20
Grade : A
DOB : 2005-06-15
Subjects : Python, DBMS, Java

Student Added Successfully!
```

---

## 🚀 Future Improvements

- Save data to a JSON file
- Load records automatically on startup
- Search student by ID
- Sort students by Name or Grade
- Input validation
- Duplicate Student ID check
- Better update interface
- Date validation
- GUI version using Tkinter
- Database version using SQLite/MySQL

---

## 🎯 Learning Outcomes

By completing this project, you will learn:

- Python Collections
- CRUD Operations
- Data Management
- Basic Project Structure
- Git & GitHub Project Hosting
- Problem Solving

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push to your branch
6. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Dharmendra Rajput**

- 🎓 Bachelor of Computer Applications (BCA)
- 💻 Python Learner
- 📊 Aspiring Data Analyst

---

⭐ If you found this project helpful, don't forget to **Star** the repository!
