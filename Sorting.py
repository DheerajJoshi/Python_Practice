#!/usr/bin/python

strs = ['aa', 'BB', 'zz', 'CC']
print sorted(strs)  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print sorted(strs, reverse=True)   ## ['zz', 'aa', 'CC', 'BB']

#there are many other ways of sorting is possible
#sorting on the basis of the number of character in the list 
#in this sorting is done on the basis of key comparision and a proxy value is 
#assigned in the sorted list
strs1 = ['ccc', 'aaaa', 'd', 'bb']
print sorted(strs1, key=len)  ## ['d', 'bb', 'ccc', 'aaaa']

#note : here in above remember for indentation which is not required so 
# be careful in using and writing the code

## "key" argument specifying str.lower function to use for sorting
#specifying "str.lower" as the key function is a way to force the sorting to tre#at uppercase and lowercase the same:
print sorted(strs, key=str.lower)  ## ['aa', 'BB', 'CC', 'zz']
