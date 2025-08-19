# File Read & Write Challenge : Create a program that reads a file and writes a modified version to a new file.
# write
file = open("recipe.txt",'w')
file.write("Here is the pilau recipe")

# read
file = open("recipe.txt",'r')
content = file.read()
print(content.upper())

# writes a modified version to a new file.
file = open("recipe_modified.txt",'w')
file.write(content.upper())
print(content.upper())
file.close()


# Error Handling Lab : Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
recipeFile = str(input("Enter the name of your file: "))
try:
    file = open(recipeFile,'r')
    new_content = file.read()
    print(new_content.upper())
    file.close()
except FileNotFoundError:
    print("File does not exist")
  
