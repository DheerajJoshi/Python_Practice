#!/usr/bin/env/python2  -tt
import subprocess
var1=raw_input("enter the link: ")
cmdping = "ping " + var1
p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()
