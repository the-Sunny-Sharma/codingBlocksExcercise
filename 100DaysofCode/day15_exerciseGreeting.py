import time
print("The current time is : ",time.strftime("%H"),":",time.strftime("%M"),":",time.strftime("%S"))
hour=int(time.strftime("%H"))
if (hour>3 and hour<12):
    print("Good Morning, Sir")
elif (hour>11 and hour<18):
    print("Good Afternoon, Sir")
else:
    print("Good Night, Sir")