#program to find the 2nd and 4th largest num in the in the given list
l = [20,30,10,4,5,2,1,100]
l.sort()
print("second largest num is",l[-2])
print("fourth largest num is",l[-4])

#using function
def largestinlist(l):
    l.sort()
    print("second largest num is", l[-2])
    print("fourth largest num is", l[-4])
l = [600,30,500,2,60]
largestinlist(l)

'''output
second largest num is 20
fourth largest num is 5
'''