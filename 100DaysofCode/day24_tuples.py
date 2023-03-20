#tupples are immutable
tup = (23,34,24,65,45)
print(type(tup),tup)

tup1 = (8) #this is not a tupple pyhton treats it as an integer 
tup2 = (8,) # this the way to create a tupple of one element
print(type(tup1),type(tup2))

#slicing creates a new tuple
newTup = tup[1:4]
print(tup,newTup)
