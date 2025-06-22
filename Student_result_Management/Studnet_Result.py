#========== Student Result Management ==========

choice = input("Enter your choice: ")


#1. First write the grade calculation function:

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 40:
        return 'D'
    else:
        return 'F'

# 2. Then write the function to add a student:

def add_student():
    print("\n--- Add New Student ---")
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    try:
        marks1 = int(input("Enter marks for Subject 1: "))
        marks2 = int(input("Enter marks for Subject 2: "))
        marks3 = int(input("Enter marks for Subject 3: "))
    except ValueError:
        print("❌ Please enter valid numeric marks.")
        return

    total = marks1 + marks2 + marks3
    average = total / 3
    grade = calculate_grade(average)

    with open("students.txt", "a") as f:
        f.write(f"{roll},{name},{marks1},{marks2},{marks3},{total},{average:.2f},{grade}\n")

    print("✅ Student record saved successfully!\n")

# 3. Write the function to view all students:

def view_students():
    print("\n--- All Student Records ---")
    try:
        with open("students.txt", "r") as f:
            for line in f:
                roll, name, m1, m2, m3, total, avg, grade = line.strip().split(",")
                print(f"Roll: {roll} | Name: {name} | Marks: [{m1}, {m2}, {m3}] | Total: {total} | Avg: {avg} | Grade: {grade}")
    except FileNotFoundError:
        print("⚠️ No records found. Please add students first.\n")


# 4. Create the main menu:

def main():
    while True:
        print("\n========== Student Result Management ==========")
        print("1. Add New Student")
        print("2. View All Records")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

#5. Final line to run the program:

if __name__ == "__main__":
    main()







