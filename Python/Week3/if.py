def myGrades():
    grade = int(input("Enter your grade:"))
    if grade >= 90:
        print("A")
    elif grade >= 80 and grade <= 89:
        print("B")
    elif grade >= 70 and grade <= 79:
        print("C")
    elif grade >= 60 and grade <= 69:
        print("D")
    else:
        print("C")




myGrades()