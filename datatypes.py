print('----integer----')
x=10
print("value of x is",x)
print("type of x is",type(x))
print("----float----")
y=1.6
print("value of y is",y)
print("type of y is",type(y))
print("---boolean----")
z=True
print("value of z is",z)
print("type of z is",type(z))
print("------lists------")
l1=[10,20,30,40,50]
l2=[60,70,80,90]
print('list l1 is',l1)
print('list l2 is',l2)
print('last ele of l1 is',l1[-1])
l3=l1+l2
print('l1+l2=',l3)
print('---------list functions-----------')
#append
l1.append(100)
print("after append",l1)
#insert
l1.insert(4,200)
print("after insert()",l1)
#pop
l1.pop()
print("after pop()",l1)
#remove
l1.remove(20)
print("after remove()",l1)
l4=[[1,2,3,4],[5,6,7,8]]
print(l4[1][3])
print("is 50 in l1?", 50 in l1)
print("is 150 in l1?", 150 in l1)
print("is 400 not in l1?", 400 not in l1)
#extend
l1.extend(l4)
print("after extend",l1)
print(l1[5][0])
print(l1[6][0])





