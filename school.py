class Student:
    def __init__(self):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.class_name = input("Enter class name: ")


class Teacher:
    def __init__(self):
        self.first_name = input("Enter teacher's first name: ")
        self.last_name = input("Enter teacher's last name: ")
        self.subject = input("Enter the subject taught: ")
        self.classes = []
        while True:
            class_name = input("Enter the class name taught by the teacher: ")
            if class_name == "":
                break
            self.classes.append(class_name)


class HomeroomTeacher:
    def __init__(self):
        self.first_name = input("Enter homeroom teacher's first name: ")
        self.last_name = input("Enter homeroom teacher's last name: ")
        self.class_name = input("Enter homeroom teacher's class name: ")


user_types = ["student", "teacher", "homeroom teacher"]
available_commands = ["create", "manage", "end"]


class Menu:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.homeroom_teachers = []
        self.classes = []

    def create_student(self):
        student = Student()
        self.students.append(student)
        print("Student added successfully")

    def create_teacher(self):
        teacher = Teacher()
        self.teachers.append(teacher)
        print("Teacher added successfully")

    def create_homeroom_teacher(self):
        homeroom_teacher = HomeroomTeacher()
        self.homeroom_teachers.append(homeroom_teacher)
        print("Homeroom teacher added successfully")

    def manage_class(self):
        class_name = input("Enter class name to display: ")
        if class_name in self.classes:
            class_displayed = class_name
#            print(f"{class_displayed} is led by {homeroom_teachers} teacher and there is student {students} - in the class")

    def manage_student(self):
        first = input("Enter student's first name: ")
        last = input("Enter student's last name: ")
        if (first, last) in self.students:
            student_displayed = (first, last)
#            print(f"")

    def manage_teacher(self):
        first = input("Enter teacher's first name: ")
        last = input("Enter teacher's last name: ")
        if (first, last) in self.teachers:
            teacher_displayed = (first, last)
#            print(f"Teacher {first, last} teaching {class_name} for {subject} ")

    def manage_homeroom_teacher(self):
        first = input("Enter homeroom teacher's first name: ")
        last = input("Enter homeroom teacher's last name: ")
        if (first, last) in self.homeroom_teachers:
            homeroom_teacher_displayed = (first, last)
#            print(f"{homeroom_teacher_displayed} is the homeroom teacher of {class_name}")

    def create_user(self):
        user = input("Enter user type: student/ teacher/ home room teacher")
        if user == "student":
            self.create_student()
        if user == "teacher":
            self.create_teacher()
        if user == "home room teacher":
            self.create_homeroom_teacher()
        if user == "end":
            return
        else:
            print("Error")

    def manage(self):
        manage = input("Enter option: class/ student/ teacher/ home room teacher")
        if manage == "class":
            self.manage_class()
        if manage == "student":
            self.manage_student()
        if manage == "teacher":
            self.manage_teacher()
        if manage == "home room teacher":
            self.manage_homeroom_teacher()
        if manage == "end":
            return
        else:
            print("Error")


while True:
    menu = Menu()
    command = input("Enter your command: create/ manage/ end \n"
                    "create - to create profile\n"
                    "manage - to display information\n"
                    "end - to terminate program\n")
    if command not in available_commands:
        print("Error, please enter valid command")
        continue
    if command == "end":
        break
    if command == "create":
        menu.create_user()
    if command == "manage":
        menu.manage()
    else:
        print("Invalid command")
        break
