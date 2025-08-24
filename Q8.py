# STUDENT INFO :
class Student:
    def __init__(self, name, rollNo, totalMarks):
        self.name = name
        self.rollNo = rollNo
        self.totalMarks = totalMarks
    
    def display(self):
        print(f"The name of the student is {self.name}.")
        print(f"The roll number of the Student is {self.rollNo}.")
        print(f"The marks obtained by the student is {self.totalMarks}")

you = input("Enter the name of the student: ")
rollNo = input("Enter the roll number of the student: ")
totalMarks = float(input("Enter the total marks obtained by the student: "))
student = Student(you, rollNo, totalMarks)
student.display()
