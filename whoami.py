'''
this is an example how to make use of python and find the present user details 
'''
import os
print os.getuid()     # numeric uid
import pwd
print pwd.getpwuid(os.getuid())   # full /etc/passwd info
# this will print result from /etc/passwd file of the present user 
