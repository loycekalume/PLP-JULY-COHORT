# a set is a collection of unique data
# elements cannot be duplicated and can be of different types and are mutable
# we put elements in curly braces


# creating an empty set we use the set function
empty_set = set()

# unlike a dictionary we just put empty curly braces{}
empty_dictionary = { }

# in set since items are unordered we do not uuse indexing or slicing

# adding an element we use add method
numbers = {20, 28,80,94}
numbers.add(32)
print(numbers)

#updating , update() method is used
new_numbers=[38,12,34,56]
numbers.update(new_numbers)
print(numbers)

# removing an element using discard() method
numbers.discard(38)
print(numbers)

# iterating over a set
for number in numbers:
    print(number)


# finding number of elements in a a set we use len() method
print(numbers)
print(len(numbers))

# union of sets combines elements to one set
A = {1,2,3,4}
B = {2,4,5,6}
print("Union of A nad B:", A | B)

# OR use union method
print("Union of A nad B:", A.union(B) )


# intersection combines elements that are both in A and B
print("Intersection of A and B using &:", A & B)

print("Intersection of A and B using intersection() method:", A.intersection(B))


# difference between sets- elements in set A thta are not in B
print("Difference of A and B using &:", A - B)

print("Difference of A and B using difference():", A.difference(B))

# Set symmetric difference - all sets in A and B without the common elements
print("using ^ :", A ^ B)
print ("using symmetric_difference()", A.symmetric_difference(B))

# Check if sets are equal
if A==B:
    print("A and B are equal")
else:
    print("They are not equal")    
