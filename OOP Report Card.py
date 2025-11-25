class Student(): # Student class
    aggregate = 0

    # Name and grades for each subject
    def __init__(self, name, english, maths, science):
        self.name = name

        self.english = english
        self.maths = maths
        self.science = science

    # Function to show grades
    def show_grades(self):
        print(f"Grade for english: {self.english}")
        print(f"Grade for maths: {self.maths}")
        print(f"Grade for science: {self.science}")

    # Function to show average
    def average(self):
        aggregate = (self.maths + self.english + self.science)/3

        print(f"{self.name}'s aggregate: {aggregate}%")

# User inputs details
name = input("Enter your name: ")
english = int(input("Enter your grade for english: "))
maths = int(input("Enter your grade for maths: "))
science = int(input("Enter your grade for science: "))

# Outputting report
student1 = Student(name, english, maths, science)
student1.show_grades()
student1.average()