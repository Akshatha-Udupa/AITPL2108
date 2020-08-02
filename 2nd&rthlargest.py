# program to find 2nd & 4th largest numbers
a = 10
b = 20
c = 5
d = 70
for i in range(0,4):
    large = 0
    if a > b and a > c and a > d:
        large = a
        a=0
    elif b > a and b >c and b > d:
        large = b
        b=0
    elif c > a and c > b and c > d:
        large = c
        c=0
    else:
        large = d
        d=0
    if i==1:
     print("second largest is ",large)
print("Fourth largest is ",large)

'''output
second largest is  20
Fourth largest is  5
'''