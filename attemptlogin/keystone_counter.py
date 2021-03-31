#!/usr/bin/env python3

loginfail = 0

with open ("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as keystone_file:
    keystone_file_lines = keystone_file.readlines()
    for line in keystone_files_lines:
        if "-----] Authorization failed" in line:
            loginfail += 1
print("The number of failed log in attempts is", loginfail)
