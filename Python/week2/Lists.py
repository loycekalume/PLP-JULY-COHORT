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

even_numbers = [2, 4, 6]
print(even_numbers)

odd_numbers = [1, 3, 5]
print(odd_numbers)
 
even_numbers.extend(odd_numbers)
print(even_numbers)
# pop- deleting an item
list1.pop(3)
print(list1) 
# delete second element
del list1[1]
print(list1) 

# delete first 2 elements
del list1[0:2]

# del last
del list1[-1]

# listing all items in a list
for item in list1:
    print(item)

    # removing element
    fruits =["orange","melon","apple","mango"]
    fruits.remove("mango")
    print(fruits)
    print(fruits.count("apple"))

    fruits.sort()
    print(fruits)

    # python list comprehension
    numbers = [number*number for number in range(1,6)]
    print(numbers)
    # [1, 4, 9, 16, 25]