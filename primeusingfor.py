#program to display prime numbers between m and n using while loop
m = 10
n = 20
for num in range(m, n):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

#using function
def prime(m,n):
    for num in range(m, n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
prime(10, 20)

''' output
11
13
17
19
'''



