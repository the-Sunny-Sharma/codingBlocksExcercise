lst = [12,34,56,67]
print(lst)
# append() adds the element to the list in the last place
lst.append(2)
print(lst)
#lst.append("stringgg")
lst.append(21)
print(lst)
# sort() sorts the list in the ascending order
lst.sort()
print(lst)
# sort(reverse=True) sorts the list in the descending order
lst.sort(reverse=True)
print(lst)
# reverse() reverses the list
lst.reverse()
print(lst)
# index() to find the index of the element(first occurance)
print(lst.index(56))
# count() counts the total number of occurance in the list 
print(lst.count(67))

###
l = [45,35,25,435,34,7]

m = l #elements of l are not copied in m, m just has the memory address refrence
m[0]=0
print(l)#this is why changing in m also changes l

### to overcome
l = [45,35,25,435,34,7] 
m = l.copy()
m[0]=0
print(l)

#insert() to insert the element in the desired index
l.insert(2,674676)
print(l)

# extend() 
newList = [7495,343,353,3423,5]
l.extend(newList) #newList to kholo and l ke end me dal do
print(l)
print(newList)

#concatination
k = l+m
print(k)