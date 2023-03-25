# we can raise custom errors by using the raise keyword

# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:
#     raise ValueError("Not a valid salary")


#defining custom errors
# class CustomError (Exception):
#     #code 
#     pass
#     try:
#         #code
#     except CustomError:
#         #code


######################################
# class CustomError (Exception):
#     if str == 'quit':
#         pass
#     else:
#         print("Enter a valid input")

# salary = input("Enter salary amount: ")
# if not 2000 < int(salary) < 5000:
#     raise ValueError("Not a valid salary")
# elif salary != 'quit':
#     raise CustomError