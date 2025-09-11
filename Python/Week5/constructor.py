class Student:
    def __init__(self, course, year=None):
        self.course = course
        self.year = year 

    def about(self):
        print(f"He is in year {self.year} does he does {self.course}")

#creating objects with unique attributes
student1 = Student("cs",4)
student2 = Student("engineering",3)

student1.about()
student2.about()


 #inheritance 
class Lecturer(Student):
    def __init__(self, name, course, department):
        self.name = name
        self.department = department
        super().__init__(course)

    def teach(self):
        print(f"Mr {self.name} teaches {self.course} in the {self.department} department.")

lecturer1 = Lecturer("Mwai","DSA","Computer Science")
lecturer2 = Lecturer("Kamau","DAA","IT")

lecturer1.teach()
lecturer2.teach()

#polymorphism
class Dog:
    def sound(self):
        print("I can bark")

class Cow:
    def sound(self):
        print("I can moo😂")

for animal in [Dog(), Cow()]:
    animal.sound()
