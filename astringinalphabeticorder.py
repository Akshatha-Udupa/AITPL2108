#Program to sort the words in a string
str = "Hello world bangalore Karnataka India"
words = str.split()
words.sort()
for word in words:
    print(word)

#using function
def sortstr(str):
    words = str.split()
    words.sort()
    for word in words:
        print(word)
str=input("Enter a string")
sortstr(str)

'''output
Hello
India
Karnataka
bangalore
world
    '''