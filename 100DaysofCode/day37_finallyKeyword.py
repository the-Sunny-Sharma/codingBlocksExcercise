# lst = [1,2,3,23,56]
# i = int(input("Enter the index"))
# try:
#     print(l[i])
# except:
#     print("Some error occured")
# finally:
#     print("I am always executed")


def div(a,b):
	try:
		print("try block is been executed")
		print("try block is terminated")
		return(a/b)
	except:
		print("Error is been encountered")
	finally:
		print("This is the finally block and we are wrapping up")
		return 108
		print("Wrapped up")

x=div(10,5)
print(x)