import getopt
import sys
import os

opt,arg = getopt.getopt(sys.argv[1:], 'i:o:')
if len(opt) != 2:
    print("enter correctly the number of arguments")
    exit()
for (op,ar) in opt:
    if op == '-i':
        text1 = ar
    elif op == '-o':
        text2 = ar
    else:
        print("enter a correct option")

if os.path.isfile(text1):
    print("the file already exists")
    file = open(text1, "r")
    contents = file.read()
    file.close()
    file2 = open(text2, 'a+')
    file2.write(contents)
    print("the content was copied")
    file2.close()
else:
    print("the file does not exists")


