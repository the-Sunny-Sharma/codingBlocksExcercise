#There are four types of arguments in pyhton: default arguments, keyword arguments, variable-length arguments and required arguments

#required arguments 
def average(a,b):
    print("the average is ",(a+b)/2)

average(8,90)

#default arguments
def avv(a=8,b=90):
    c = (a+b)/2
    print("the average is ",(a+b)/2)
    return c

avv()
v = avv(8)
print(v)
avv(b=89)

#keyword arguments
def keyave(a,b,c):
    print("the average is ",(a+b+c)/3)

keyave(8,7,5)
keyave(c=5,a=8,b=7)

#variable-length argument
#2 ways 1.arbitrary arguments 2.keyword-arbitrary arguments

def name(*name):
    print("hello", name[0],name[1],name[2])

name("Rubina","Durga","Laxmi")

def keyword(*nums): #takes arguments as a tuple
    type(nums)
    sum =0
    for i in nums:
        sum = sum + i
    print("average is = ",sum/len(nums))

keyword(1,2,3,45)
keyword(4,5)

#2.keyword-arbitrary arguments

def nname(**name):
    type(name)
    print("hello",name["fname"],name["mname"],name["surname"])
nname(mname="Sudhir",surname="Pandey",fname="Bahadur")

