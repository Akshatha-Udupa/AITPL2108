# program to find 3rd & 5th smallest numbers
a = 10
b = 20
c = 5
d = 70
e = 100
max = max(a,b,c,d)
max = max+1
for i in range(0,5):
    small = 0
    if a < b and a < c and a < d and a < e:
        small = a
        a = max
    elif b < a and b < c and b < d and b < e:
        small = b
        b = max
    elif c < a and c < b and c < d and c < e:
        small = c
        c = max
    elif d < a and d < b and d < c and d < e:
        small = d
        d = max
    else:
        small = e
        e = max
    if i == 2:
     print("third smallest is ",small)
print("Fifth smallest is ",small)

'''output
third smallest is  20
Fifth smallest is  100

'''