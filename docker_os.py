#! /usr/bin/python3
print("content-type:text/html")
print()

import subprocess
import cgi

form = cgi.FieldStorage()

os_name = form.getvalue("x")
image = form.getvalue("y")

cmd = "sudo docker run -d -i -t --name {0} {1}".format(os_name,image)

output = subprocess.getstatusoutput(cmd)
status = output[0]
os_id = output[1]

print("{0} has successfully launched with id : {1}".format(os_name,os_id))
