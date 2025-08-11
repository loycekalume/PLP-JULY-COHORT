# list
# starts from index 0
# can have differet data types

list1 = [1,2,3,4,5]
print(list1)


# adding an item at the end
list1.append(3)
print(list1)

list1.insert(len(list1),6)
print(list1)


# extend() → takes each element from the other list (or iterable) and merges them into one continuous list.
list1.extend([8,9])
print(list1)
# [1, 2, 3, 4, 5, 3, 6, 8, 9]

# append() → adds the entire other list as one single element, which creates a nested list.
list1.append([10,11])
print(list1) 
# [1, 2, 3, 4, 5, 3, 6, 8, 9, [10, 11]]


# pop- deleting an item
list1.pop(3)
print(list1) 

del list1[1]
print(list1) 

# listing all items in a list
for item in list1:
    print(item)