for i in range(43):
    print(i) #0-42
else:
    print("Loop executed successfully")

#Syntax
# for couonter in sequence:
#     Statements inside for loop block
# else:
#     Statements inside else block

for i in range(43):
    print(i) #0-42
    if i == 5:
        break  #else will not be executed
else:
    print("Loop executed successfully")

#while with else
i = 0
while  i < 34:
    print(i) #0-42
    # if i == 5:
        # break  #else will not be executed
    i += 1
else:
    print("Loop executed successfully")