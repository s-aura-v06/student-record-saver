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
