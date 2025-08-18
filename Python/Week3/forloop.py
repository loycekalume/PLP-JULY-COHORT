# prints every item-iterates through each item
fruits = ["apple","melon","mango","pineapple","orange"]
for fruit in fruits:
    print(f"I like {fruit} !")

# for in range - prints from the first number in range but does not include the last number
for number in range (1,6):
    print(f"These are numbers we got: {number} ")
    # prints 1,2,3,4,5 - leaves out the last number


# while loop - iloops through as long as the given condition is true
count = 0
while count <=6:
    print(f"Number:{count}")
    count += 1

# break and continue
for number in range (1,10):
    if number == 9:
        print(f"i want to break at number {number}")
        break
    elif number % 2 ==0:
        print(f"Skipping this number {number} because it's even!")
        continue
    print(f"This is the number:{number}")


# inner and outer loop
for number in range (1,4):
    print(f"Number in outerloop:{number}")
    for number in range (1,4):
        print(f"Number in innerloop:{number}")

students = ["Loyce","Bob"]
subjects = ["Maths","Science","Business"]
for student in students:
    print(f"Student 1: {student}")
    for subject in subjects:
        print(f"- {subject}")