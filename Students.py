class Student:

    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.courses = {}

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = []

    def add_grades(self, course_name, grade):
        if course_name in self.courses.keys():
            self.courses[course_name].append(grade)
        else:
            print(f"{course_name} not found . Please add course before")

    def average_grade(self):
        total = 0
        count = 0
        for grades in self.courses.values():
            total = sum(grades)
            count = len(grades)
        return total / count if count != 0 else 0

    def __str__(self):
        return f"Student: {self.first_name},{self.last_name},id:{self.id} Average Grade: {self.average_grade():.2f}"


student1 = Student("Yana", "Kaufman", 326956638)
student2 = Student("Dmitry", "Kaufman", 319251518)

student1.add_course("Math")
student1.add_course("English")
student1.add_course("Economic")

student2.add_course("Math")
student2.add_course("English")
student2.add_course("PC")

student1.add_grades("Math", 90)
student1.add_grades("English", 100)
student1.add_grades("Economic", 85)
print(student1)
student2.add_grades("Math", 90)
student2.add_grades("English", 85)
student2.add_grades("PC", 95)
print(student2)
