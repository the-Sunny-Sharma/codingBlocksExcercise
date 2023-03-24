
#dictionaries are ordered ds, but it was not the case at first later v-3.6 and prev
info = {'name' : 'Karan',
        'age' : 19,
        'eligible': True}
print(info)

#this may throw an error if the key value is not found
print(info['age'])

#this will print "None" if the key value is not found
x = info.get("age2")
print(x)


print(info.keys())
print(info.values())
# for key in info.keys():
#     print(info[key])
    
for key in info.keys():
    print(f"{key} = {info[key]}")

#packed in tupples
print(info.items())
#unpacked 
for key,value in info.items():
    print(f"The value corresponding to the key {key} is {value}")