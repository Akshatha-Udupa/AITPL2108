#program to  check whether given no is prime or not
num = 0
if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            Flag=0
            break
        else:
            Flag=1
    if Flag == 1:
        print("{0} is prime number".format(num))
    else:
        print("{0} is not prime number".format(num))

else:
    print("{0} is not prime number".format(num))

#using function

def prime(num):
    if num > 1:
        for i in range(2, num // 2):
            if (num % i) == 0:
                Flag = 0
                break
            else:
                Flag = 1
        if Flag == 1:
            print("{0} is prime number".format(num))
        else:
            print("{0} is not prime number".format(num))

    else:
        print("{0} is not prime number".format(num))
prime(num=int(input("Enter a number")))
'''output
0 is not prime number
'''