l = [2,3,4,5]
print(type(l))
print(l)
print(l[0])
if 4 in l:
    print("Yes")
else:
    print("no")
#operations such as slicing and jump indexing can also be performed as same in strings
#
#list comprehension
#SYNTAX: List = [Expression(item) for item in iterable if Condition]
lis = [i for i in range(20)]
print(lis) 

lis = [i*i for i in range(20)]
print(lis) 