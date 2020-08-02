#program to display prime numbers between m and n using while loop
m = 0
n = 10
flag = 0
while m <= n:
    if m > 1:
        i = 2
        while i <= m / 2:
            if m % i == 0:
                flag = 1
                break
            else:
                flag = 0
                i = i+1
        if flag == 0:
            print(m)
        m = m + 1
    else:
        m = m + 1
#using function
def prime(m,n):
    flag = 0
    while m <= n:
        if m > 1:
            i = 2
            while i <= m / 2:
                if m % i == 0:
                    flag = 1
                    break
                else:
                    flag = 0
                i = i+1
            if flag == 0:
                print(m)
            m = m + 1
        else:
            m = m + 1
prime(10,20)
''' output
11
13
17
19
'''



