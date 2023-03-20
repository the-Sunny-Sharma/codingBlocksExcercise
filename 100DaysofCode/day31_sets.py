#sets does not contain repeated values
#sets contain unordered data

info = {"Carla",19,False,5.3,19}
print(info) #OUTPUT: {'Carla', False, 19, 5.3}


emptySet = set() #empty set
print(type(emptySet))

for i in info:
    print(i)
    #False
    # 19
    # Carla
    # 5.3

    