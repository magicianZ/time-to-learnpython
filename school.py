class Student:
    def __init__(self,name):
        self.name = name
        
class College_Student(Student):
    def __init__(self,name,degree):
        super().__init__(name)
        self.degree = degree





Mr_Whalen = College_Student("Mr Whalen","Master in Computer Sdcience")

print(Mr_Whalen)