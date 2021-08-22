# This is my TWY Calculculator.
# Date: 21/08/2021
# Author: Yash Vardhan

while True:
    print("Enter A For Addition")
    print("Enter S For Subtraction")
    print("Enter M For Multiplication")
    print("Enter D For Division")
    print("Enter Q To Quit")

    choice = input("Enter Your Choice: ")

    if choice == 'Q':
        break
    elif choice == 'A':
        num1 = float(input("Enter The First Number: "))
        num2 = float(input("Enter The Second Number: "))
        print(num1+num2)
    elif choice == 'S':
        num1 = float(input("Enter The First Number: "))
        num2 = float(input("Enter The Second Number: "))
        print(num1-num2)
    elif choice == 'M':
        num1 = float(input("Enter The First Number: "))
        num2 = float(input("Enter The Second Number: "))
        print(num1*num2)
    elif choice == 'D':
        num1 = float(input("Enter The First Number: "))
        num2 = float(input("Enter The Second Number: "))
        if num2 == 0:
            print("The Anwer Is Infinite")
        else:
            print(num1/num2)
    else:
        print("Invalid Choice")