#! /usr/bin/python3
print("content-type:text/html")
print()

import subprocess
import cgi

cmd = cgi.FieldStorage()
cmd = cmd.getvalue("x")

op = subprocess.getoutput(cmd)
print(op)
