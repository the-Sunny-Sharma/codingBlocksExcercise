#try except code
#To prevent the program termination without executing the program completely
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
# except Exception as e:
#     print(e)
except:
    print("invalid input")

print("Some imp lines of code")
print("End of program")


#we can even handle the specific error


# try:
#     for i in range(1,11):
#         print(f"{a} X {i} = {int(a)*i}")
# # except Exception as e:
# #     print(e)
# except ValueError:
#     print("value error")
# except IndexError:
#     print("invalid input")


print("Some imp lines of code")
print("End of program")
