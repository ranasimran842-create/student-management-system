class Student:

    def __init__(self, s_id, s_name, s_age, s_marks):
        self.s_id = s_id
        self.s_name = s_name
        self.s_age = s_age
        self.s_marks = s_marks

    def display(self):
        print("\nStudent ID :", self.s_id)
        print("Student Name :", self.s_name)
        print("Student Age :", self.s_age)
        print("Student Marks :", self.s_marks)


class StudentManagementSystem:

    def __init__(self):
        self.students = []

    def add_student(self):
        s_id = int(input("Enter ID: "))
        s_name = input("Enter Name: ")
        s_age = int(input("Enter Age: "))
        s_marks = float(input("Enter Marks: "))

        student = Student(s_id, s_name, s_age, s_marks)
        self.students.append(student)

        print("Student added successfully!")


    def view_students(self):
        if len(self.students) == 0:
            print("No students found")
        else:
            for student in self.students:
                student.display()


    def search_student(self):
        s_id = int(input("Enter Student ID: "))

        for student in self.students:
            if student.s_id == s_id:
                student.display()
                return

        print("Student not found")


    def update_marks(self):
        s_id = int(input("Enter Student ID: "))

        for student in self.students:
            if student.s_id == s_id:
                new_marks = float(input("Enter new marks: "))
                student.s_marks = new_marks
                print("Marks updated successfully!")
                return

        print("Student not found")


    def delete_student(self):
        s_id = int(input("Enter Student ID: "))

        for student in self.students:
            if student.s_id == s_id:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found")


    def display_topper(self):

        if len(self.students) == 0:
            print("No students available")
            return

        topper = self.students[0]

        for student in self.students:
            if student.s_marks > topper.s_marks:
                topper = student

        print("\nTopper Details:")
        topper.display()



sms = StudentManagementSystem()


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Display Topper")
    print("7. Exit")


    choice = int(input("Enter your choice: "))


    if choice == 1:
        sms.add_student()

    elif choice == 2:
        sms.view_students()

    elif choice == 3:
        sms.search_student()

    elif choice == 4:
        sms.update_marks()

    elif choice == 5:
        sms.delete_student()

    elif choice == 6:
        sms.display_topper()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid choice!")