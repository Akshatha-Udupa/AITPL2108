#WAP to check whether  the given number is postive negative or zero number without using if for or while
def index(i):
    return 1 + (i >> 31) - (-i >> 31)
def check(n):
   s = "negative", "zero", "positive"
   val = index(n)
   print(n, "is", s[val])
check(10)

'''output
10 is Positive
'''