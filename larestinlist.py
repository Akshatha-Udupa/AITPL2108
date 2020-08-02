#program to find the largest num in the in the given list
l = [10,30,500,2,60]
l.sort()
print("{0} Largest number in a list ".format(l[-1]))

#using function
def largestinlist(l):
    l.sort()
    print("{0} Largest number in a list ".format(l[-1]))
l = [600,30,500,2,60]
largestinlist(l)

'''output
500 Largest number in a list 
'''