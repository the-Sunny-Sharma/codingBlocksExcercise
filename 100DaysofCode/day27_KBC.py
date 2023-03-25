print("WELCOME TO KBC")
ques1 = "The International Literacy Day is observed on"
opt1 = """A. Sep 8      B. Nov 28
C. May 2        D. Sep 22"""
ans1 = "A"

ques2 = "The language of Lakshadweep. a Union Territory of India, is"
opt2 = """A. Tamil      B. Hindi
C. Malayalam        D. Telugu"""
ans2 = "C"

ques3 = "In which group of places the Kumbha Mela is held every twelve years?"
opt3 = """A. Ujjain. Purl; Prayag. Haridwar      B. Prayag. Haridwar, Ujjain,. Nasik
C. Rameshwaram. Purl, Badrinath. Dwarika        D. Chittakoot, Ujjain, Prayag,'Haridwar"""
ans3 = "B"


KBCques = (ques1,ques2,ques3)
KBCopt = (opt1,opt2,opt3)
KBCans = (ans1,ans2,ans3)

#questions = 0,3,6
#opt= 1,4,7
#ans = 2,5,8

var = len(KBCques)
print(var)

for i in range(var):
    print("Here is the Question on your screen")
    print(KBCques[i])
    print("And the options are \n",KBCopt[i])

    answer = input()
    

    print("Are you sure about the option ",answer,"\n Y or N?")

    confirmation = input()
    if confirmation == "Y" or "y":
        if(answer == KBCans[i]):
            print("It's absoulutely the right answer")
        else:
            print("Better luck next time")
            break





