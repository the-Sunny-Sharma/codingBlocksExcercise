#since tuple are immutuable we cannot perform operations such as insert, delete, etc
#rather we can first it to list, then perform the operations and at last convert it back to tuple

countries=("Spain", "Russia", "India", "Finland", "Germany")
temp = list(countries)
temp.append("England")  #add
temp.pop(1) #remove
temp[0]="Sri Lanka"
countries=tuple(temp)
print(countries)

#we can concatinate,count(),index(element,starting,ending),len(),etc.
