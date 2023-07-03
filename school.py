class Student:
    def __init__(self):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.class_name = input("Enter class name: ")

class Teacher:
    def __init__(self):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.subject = input("Enter subject: ")
        self.classes = input("Enter class name: ")

class HomeroomTeacher:
    def __init__(self):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.class_name = input("Enter class name: ")

user_types = ["student", "teacher", "homeroom teacher"]
available_commands = ["create", "manage", "end"]

class Menu:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.homeroom_teachers = []
    def create_student(self):
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        class_name = input("Enter student's class name: ")
        student = Student()
        self.students.append(student)
        print("Student added successfully")

    def create_teacher(self):
        first_name = input("Enter teacher's first name: ")
        last_name = input("Enter teacher's last name: ")
        subject = input("Enter the subject taught: ")
        classes = []
        while True:
            class_name = input("Enter the class name taught by the teacher: ")
            if class_name == "":
                break
            classes.append(class_name)
        teacher = Teacher()
        self.teachers.append(teacher)
        print("Teacher added successfully")

    def create_homeroom_teacher(self):
        self.first_name = input("Enter homeroom teacher's first name: ")
        self.last_name = input("Enter homeroom teacher's last name: ")
        self.class_name = input("Enter homeroom teacher's class name: ")
        homeroom_teacher = HomeroomTeacher()
        self.homeroom_teachers.append(homeroom_teacher)
        print("Homeroom teacher added successfully")

    while True:
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
            self.create_user()
        if command == "manage":
            self.manage_user()
        else:
            print("Invalid command")
            break

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

    #def manage_class(self):
    #    class_search = input("Enter class name to display")
    #    if class_search in classes:
    #        print(f"Student in class {class_search}")


