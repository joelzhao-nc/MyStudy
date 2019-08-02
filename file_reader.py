import os

basedir = os.path.dirname(__file__)
print(basedir)

filename_1=basedir+'/1.py'

filename_3='1.txt'

with open(filename_3) as file_object:
    contents=file_object.read()
    print(contents.rstrip())

filename_2=basedir+'/11.py'


pi_string=''
with open(filename_2) as file_obj:
    for line in file_obj:
        pi_string+=line.rstrip()
print(pi_string)
print(len(pi_string))