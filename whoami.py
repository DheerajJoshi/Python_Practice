'''
here I am using Python 2X
this is an example how to make use of python and find the present user details 
'''
import os
print os.getuid()     # numeric uid
import pwd
print pwd.getpwuid(os.getuid())   # full /etc/passwd info
# this will print result from /etc/passwd file of the present user 


'''
second alternative way to directly print the name of the user 
'''

import getpass
print getpass.getuser()




'''
getpass.getuser()

Return the “login name” of the user. Availability: Unix, Windows.

This function checks the environment variables LOGNAME, USER, LNAME and 
USERNAME, in order, and returns the value of the first one which is set
to a non-empty string. If none are set, the login name from the password
database is returned on systems which support the pwd module, otherwise,
an exception is raised
'''

'''
next way to do this 
'''
name = os.popen('whoami').read() 

#But that has to start a whole new process.

os.environ["USER"]

#works sometimes, but sometimes that environment variable isn't set.
#print name

