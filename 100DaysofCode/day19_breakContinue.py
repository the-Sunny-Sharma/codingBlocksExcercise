for i in range(20):
    if(i==10):
        print("10 is last")
        break
    elif(i==5):
        print("chal 5")
        continue
    print(i) 

#do while loop
while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number >0 :
        break