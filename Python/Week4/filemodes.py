# write
file = open("newFile.pdf",'w')
file.write("I bought bread and mandazi today\n")
print("File created successfully")

# read
file = open("newFile.pdf",'r')
content = file.read()
print(content)

# append
file = open("newFile.pdf",'a')
file.write("I prepared breakfast too")

file = open("newFile.pdf",'r')
content = file.read()
print(content.upper())
words = content.split()
words_count = len(words)
print(f"There are {words_count} words in this file.")


# error handling
try:
    file = open("newFile.txt",'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("File operation completed")
    file.close()
