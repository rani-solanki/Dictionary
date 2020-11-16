user=int(input("enter the number"))
if (user%4==0 and user%100!=0):
    print("yes")
elif user%400==0:
    print("yes")
else:
    print("simple")
    