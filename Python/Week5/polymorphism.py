class Student:
    def role(self):
        print("I am a student")

class Lecturer:
    def role(self):
        print("I am a lecturer")       

for person in [Student(), Lecturer()]:
    person.role()


class Dog:
    def sound(self):
        print("I can bark")

class Cow:
    def sound(self):
        print("I can moo😂")

for animal in [Dog(), Cow()]:
    animal.sound()
