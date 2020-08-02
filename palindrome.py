#:python pgm to check whether string is palindorme or not
str="malayalam"
str=str.casefold()
if str==str[::-1]:                       # check whether given string & reverse of a string are same
    print("Given string {0} is palindrome".format(str))
else:
    print("Given string {0} is not palindrome".format(str))

#using function

def palindrome(str):
    str=str.casefold()
    if str==str[::-1]:
        print("Given string {0} is palindrome".format(str))
    else:
        print("Given string {0} is not palindrome".format(str))
palindrome("bangalore")

''' Output
for string "malayalam"
Given string malayalam is palindrome

for string "bangalore"
Given string bangalore is not palindrome
'''
