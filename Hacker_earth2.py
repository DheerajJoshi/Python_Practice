'''
this is one of the another question I have faced in hackerearth and below is the solution of what I have done .
we just have to find out the difference of the sum of diagonal elements.
I have also submitted the code in C++ but below code is in Python.
'''
#!/usr/bin/python
n=input()
arr=[]
for _ in range(n) : 
	temp=map(int,raw_input().split())
	arr.append(temp)
s1,s2=0,0
for i in range(n) :
	s1 +=arr[i][i]
	s2 +=arr[-i-1][i]
print abs(s1-s2)
