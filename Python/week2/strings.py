# slicing-getting a specific part of a string
name ='Loyce'
print(name[1:4])
# output - oyc

# we can create multiline string using """
message = """
Hello friends today i learnt a lot about python 
data structures.They include: sets, lists, tuples,
and dictionaries.It was fun reminding myself this.
"""
print (message)

# joining strings
gender = "female"
joined = name + gender
print(joined)

# iterating in a string
for letter in name:
    print(letter)

# string formatting
print(f'{name} is {gender}')

# escape sequence
example = "He said,\"What's there\""