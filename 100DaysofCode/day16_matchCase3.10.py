#match cases were introduced in python from version 3.10
abc = int(input("Enter a number: "))
match abc:
    case 0:
        print("Zero")
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case _ if abc<=10:
        print(abc)
    case _:
        print("Number exceeds 10")