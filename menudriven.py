#Menu driven program to perform arithmetic opearations
loop = 'y'
while loop == 'y':
    print(" 1. Add\n 2. Subtract\n 3. Multiply\n 4. Division\n 5. Modulus\n 6.Floor division")
    ch = int(input("Enter your choice "))
    if ch == 1:
        a = int(input("Enter 1st number "))
        b = int(input("Enter 2nd number "))
        c = a + b
        print("Addition of {0} and {1} is {2} ".format(a,b,c))
    elif ch == 2:
        a = int(input("Enter 1st number "))
        b = int(input("Enter 2nd number "))
        c = a - b
        print("Subtraction of {0} and {1} is {2} ".format(a,b,c))
    elif ch == 3:
        a = int(input("Enter 1st number "))
        b = int(input("Enter 2nd number "))
        c = a * b
        print("Multiplication of {0} and {1} is {2} ".format(a,b,c))
    elif ch == 4:
        a = int(input("Enter 1st number "))
        b = int(input("Enter 2nd number "))
        c = a / b
        print("Division of {0} and {1} is {2} ".format(a,b,c))
    elif ch == 5:
        a = int(input("Enter 1st number "))
        b = int(input("Enter 2nd number "))
        c = a % b
        print("Modulus of {0} and {1} is {2} ".format(a, b, c))
    elif ch == 6:
        a = int(input("Enter 1st number "))
        b = int(input("Enter 2nd number "))
        c = a // b
        print("Floor division of {0} and {1} is {2} ".format(a, b, c))
    else:
        print("Invalid choice")
    loop = input("Do you want to continue?(Y/N)")
    loop = loop.casefold()

'''OUTPUT
1. Add
 2. Subtract
 3. Multiply
 4. Division
 5. Modulus
 6.Floor division
Enter your choice 1
Enter 1st number 10
Enter 2nd number 20
Addition of 10 and 20 is 30 
Do you want to continue?(Y/N)Y
 1. Add
 2. Subtract
 3. Multiply
 4. Division
 5. Modulus
 6.Floor division
Enter your choice 2
Enter 1st number 20
Enter 2nd number 3
Subtraction of 20 and 3 is 17 
Do you want to continue?(Y/N)N
'''