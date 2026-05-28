# student-record-saver
My first Python project

📚 Student Record Management System (Python)

📌 Project Description

This is a simple Python-based Student Record Management System that uses file handling to store and display student information. The program takes input from the user such as student name, age, and marks, and stores the data in a text file named students.txt.

The system allows multiple entries using a loop and keeps adding new records without deleting previous data. It uses file handling concepts like append mode to store data and read mode to display all saved records.

Through this project, I learned how to use Python basics such as input/output operations, loops, and file handling techniques to manage data efficiently.

✨ Features
Add multiple student records
Store data in a text file
Uses file handling (write & read operations)
Loop-based input system
Simple console-based interface
Displays all stored student records

💻 Technologies Used
Python 3
File Handling
Loops (while loop)
Input/Output operations

📂 Code
while True:

    name = input("Enter student name: ")
    age = input("Enter age: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Marks: {marks}\n")
        file.write("-------------------\n")

    choice = input("Do you want to add more? (yes/no): ")

    if choice == "no":
        break

print("\nStudent Records:\n")

with open("students.txt", "r") as file:
    data = file.read()
    print(data)
    
🚀 Learning Outcome
Understood file handling in Python
Learned how to store structured data in text files
Improved understanding of loops and user input handling
Built a basic real-world mini project
