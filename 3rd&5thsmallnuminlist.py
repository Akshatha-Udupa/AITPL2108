#program to find the 3rd and 5th smallest num in the in the given list
l = [20,30,10,4,5,70,28]
l.sort()
print("third smallest num is",l[2])
print("Fifth smallest num is",l[4])

#using function

def smallest(l):
    l.sort()
    print("third smallest num is", l[2])
    print("Fifth smallest num is", l[4])
l = [600,30,500,2,60]
smallest(l)

'''output
third smallest num is 60
Fifth smallest num is 600
'''