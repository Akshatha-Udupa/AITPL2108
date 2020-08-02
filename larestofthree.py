#largest of 3 numbers
a = 100
b= 500
c = 00
if a > b and a > c:
    print("{0} is largest number".format(a))
elif b > c:
    print("{0} is largest number".format(b))
else:
    print("{0} is largest number".format(c))

#using function

def largest(a,b,c):
    if a > b and a > c:
        print("{0} is largest number".format(a))
    elif b > c:
        print("{0} is largest number".format(b))
    else:
        print("{0} is largest number".format(c))
largest(0,1,1)

'''output
500 is largest number

'''