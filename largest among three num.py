a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a third number: "))
if a>=b and a>=c:
    print(f"{a} is a greater number")
elif b>=a and b>=c:
    print(f"{b} is a greater number")    
else:
    print(f"{c} is a greater")    