def summary(ILS,Euro,USD):
    count = ILS + (Euro*3.9) + (USD*3.4)
    print("I have " + str(count) + " ILS")
    return count

def tax(a,b,c):
    ddddd=summary(a,b,c)
    print(ddddd*1.17)

        True
        False


######################main dev

a = int(input("Enter how many shekels: "))
b = int(input("Enter how many EURO: "))
c = int(input("Enter how many USD: "))
choose=input("You want to pay tax free? y/n ")
if choose == "y":
    summary(a,b,c)
else:
    tax(a,b,c)