#!/usr/bin/python
def User():
    i,j = 0,0
    s = raw_input('Enter String')
    print "+",
    while(i < len(s)):
        print "-",
        i = i +1
    print "+"
    print "|  ",
    print s, "    |"
    print "+",
    while(j < len(s)):
        print "-",
        j = j + 1
    print "+"

User()

'''
the output of the file will display whatever the user enter inside the rectangle box in a nice way
'''
