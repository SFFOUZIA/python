students = {
    "Alice": 85,
    "Sara": 92,
    "Aisha": 88
}

name = input("Enter the student's name: ")

found = False

for key in students:
    if key.lower() == name.lower():
        print(f"{key}'s marks are: {students[key]}")
        found = True
        break


if not found:
    print("Student not found.")