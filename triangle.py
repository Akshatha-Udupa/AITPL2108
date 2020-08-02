#program to print a triangle of no of 0 & 1
def binaryRightAngleTriangle(n):
    for row in range(0, n):
        for col in range(0, row + 1):
            if (((row + col) % 2) == 0):
                print("0", end="")
            else:
                print("1", end="")
            print("\t", end="")
        print("")
n = int(input("Enter no of rows: "))
binaryRightAngleTriangle(n)


'''output
Enter no of rows: 4
0	
1	0	
0	1	0	
1	0	1	0	
'''