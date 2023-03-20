# a = 9
# b= 8
# geoMean = (a-b)/(a+b)
# print(geoMean)

# c = 95
# d = 83
# geoM = (c-d)/(c+d)
# print(geoM)

#function
def calGeoMean(x,y): #user-defined function
    Mean = (x-y)/(x+y)
    print(Mean)

def calMean(a,b): #empty function
    pass

calGeoMean(9,8) 

print(callable(calGeoMean)) #built-in function

