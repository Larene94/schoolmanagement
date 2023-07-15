class Student:
    def __init__(self, menu):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.class_name = input("Enter class name: ")
        group = menu.get_group(self.class_name)
        group.students.append(self)


class Teacher:
    def __init__(self):
        self.first_name = input("Enter teacher's first name: ")
        self.last_name = input("Enter teacher's last name: ")
        self.subject = input("Enter the subject taught: ")
        self.classes = []
        while True:
            class_name = input("Enter the class name taught by the teacher: (Press 'ENTER' to complete it)")
            if class_name == "":
                break
            self.classes.append(class_name)


class HomeroomTeacher:
    def __init__(self):
        self.first_name = input("Enter homeroom teacher's first name: ")
        self.last_name = input("Enter homeroom teacher's last name: ")
        self.class_name = input("Enter homeroom teacher's class name: ")


class Group:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.teachers = []
        self.homeroom_teacher = None


class Menu:
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.homeroom_teachers = {}
        self.classes = {}

    def get_group(self, class_name):
        if class_name not in self.classes:
            group = Group(class_name)
            self.classes[class_name] = group
        return self.classes[class_name]

    def create_student(self):
        student = Student(self)
        self.students[student.first_name, student.last_name] = student
        print("Student added successfully")

    def create_teacher(self):
        teacher = Teacher()
        self.teachers[teacher.first_name, teacher.last_name] = teacher
        print("Teacher added successfully")

    def create_homeroom_teacher(self):
        homeroom_teacher = HomeroomTeacher()
        self.homeroom_teachers[homeroom_teacher.first_name, homeroom_teacher.last_name] = homeroom_teacher
        print("Homeroom teacher added successfully")

    def manage_class(self):
        class_name = input("Enter class name to display: ")
        if class_name in self.classes:
            group = self.classes[class_name]
            if group.homeroom_teacher:
                print(f"{group.homeroom_teacher.first_name} {group.homeroom_teacher.last_name}")
            else:
                print("No homeroom teacher found")
            for student in group.students:
                print(f"Student: {student.first_name} {student.last_name}")

    def manage_student(self):
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        if (first_name, last_name) in self.students:
            student = self.students[(first_name, last_name)]
            print(f"Student: {student.first_name} {student.last_name}")
            group = self.get_group(student.class_name)
            print(f"Class: {group.class_name}")
            for teacher in group.teachers:
                if student.class_name in teacher.classes:
                    print(f"Teacher: {teacher.first_name} {teacher.last_name}")
                    print(f"Teaching subject: {teacher.subject}")
        else:
            print("Student not found.")

    def manage_teacher(self):
        first_name = input("Enter teacher's first name: ")
        last_name = input("Enter teacher's last name: ")
        if (first_name, last_name) in self.teachers:
            teacher = self.teachers[(first_name, last_name)]
            print(f"Teacher: {teacher.first_name} {teacher.last_name}")
            print(f"Teaching subjects: {teacher.subject}")
            for class_name in teacher.classes:
                print(f"Class: {class_name}")
        else:
            print("Teacher not found.")

    def manage_homeroom_teacher(self):
        first_name = input("Enter homeroom teacher's first name: ")
        last_name = input("Enter homeroom teacher's last name: ")
        if (first_name, last_name) in self.homeroom_teachers:
            homeroom_teacher = self.homeroom_teachers[(first_name, last_name)]
            print(f"Homeroom Teacher: {homeroom_teacher.first_name} {homeroom_teacher.last_name}")
            print(f"Class: {homeroom_teacher.class_name}")
            group = self.get_group(homeroom_teacher.class_name)
            for student in group.students:
                print(f"Student: {student.first_name} {student.last_name}")
        else:
            print("Homeroom teacher not found.")

    def create_user(self):
        user = input("Enter user type: student/ teacher/ homeroom teacher\n")
        if user == "student":
            self.create_student()
        if user == "teacher":
            self.create_teacher()
        if user == "homeroom teacher":
            self.create_homeroom_teacher()
        if user == "end":
            return
        else:
            print("Invalid user type")

    def manage(self):
        manage = input("Enter option: class/ student/ teacher/ homeroom teacher")
        if manage == "class":
            self.manage_class()
        if manage == "student":
            self.manage_student()
        if manage == "teacher":
            self.manage_teacher()
        if manage == "homeroom teacher":
            self.manage_homeroom_teacher()
        if manage == "end":
            return
        else:
            print("Invalid option")


menu = Menu()

while True:
    command = input("Enter your command: create/ manage/ end \n"
                    "create - to create profile\n"
                    "manage - to display information\n"
                    "end - to terminate program\n")
    if command == "create":
        menu.create_user()
    if command == "manage":
        menu.manage()
    if command == "end":
        break
    else:
        print("Invalid command")
