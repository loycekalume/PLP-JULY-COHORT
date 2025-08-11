# tuples are initialized using parenthesis
# one item is string
# starts from index 0
name =("hello")
print(type(name))
 
#  once they have more than one item then it is a tuple
name1 =("hello",)
print(type(name1))

# only two methods are used in tuples since they are immutable
# count and index
my_tuple = ("apple","melon","orange","apple")
print(my_tuple.count("apple"))
print(my_tuple.index("melon"))