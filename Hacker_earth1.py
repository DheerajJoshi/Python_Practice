#!/usr/bin/python
'''
this code is for taking the two integer without being concerned to the 
EOF and this is done by the below concept.

'''
def solveMeSecond(a,b):
   return a+b
n=int(raw_input())
for i in range(0,n) :
	a,b=raw_input().split()
	#above code will place the value in the list
        #or one more code is possible after which no need to write the next line
        # a,b=map(int,raw_input().split())
	a,b=int(a),int(b)
#above line will convert the string type to the integer type

#calling of function takes place and passing the argument a and b 

	res=solveMeSecond(a,b)
	print res
