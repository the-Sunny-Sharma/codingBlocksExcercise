#python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)

square(5) 
print(square.__doc__)

print(print.__doc__) #(func.__doc__)

#Difference between comments and docstrings
#Comments
#comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.
#Docstrings
#docstrings are right after/above the definition of a function, method, class, or module. They are used to document our code.


#wrong way
# def square(n):
#     print(n)
#     '''Takes in a number n, returns the square of n'''
#     print(n**2)

#PEP 8
#the Zen of python

#try 
import this
