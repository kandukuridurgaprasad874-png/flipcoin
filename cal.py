def call():
    print("1.add")
    print("2.sub")
    print("3.multi")
    print("4.div")
    option=int(input("choose the options: "))
    num1=int(input("Enter the first num: ")) 
    num2=int(input("Enter the second num: "))  
    if option == 1:
        print(num1 + num2)
    elif option == 2:
        print(num1 - num2)
    elif option == 3:
        print(num1 * num2)
    elif option == 4:
        print(num1 // num2)
    else:
        print("Invalid option")       
