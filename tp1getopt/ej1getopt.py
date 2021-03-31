
import sys 
import getopt

opt,arg = getopt.getopt (sys.argv[1:], 'o:n:m:')
if len(opt) != 3:
    print("enter correctly the number of parameters")
    exit()

for (op,ar) in opt:
    if op == '-o':
        operator = ar
    if op == '-n':
        number1 = int(ar)
    if op == '-m':
        number2 = int(ar)
def calculator(operator,number1,number2):
    if operator == '+':
        print(number1+number2)
    elif operator == '-':
        print(number1-number2)
    elif operator == '*':
        print(number1*number2)
    elif operator == '/':
        print(number1/number2)

if operator in ["+","-","*",""]:
    calculator(operator,number1,number2)
else:
    print ("The operator is invalid, please just use +, -, *, /")
    