import sys
import getopt
from os import getpid, fork, getppid

 opt,arg = getopt.getopt(sys.argv[1:], 'n:')
    if len(opt) != 1:
        print("Correctly enter the number of arguments")
        exit()


def show_process():
    process_son_id = getpid()
    father_id = getpid()
    print(f'Im the process, {process_son_id}, and my father is: {father_id}')
    exit()

son_number = 0
for (op,ar) in opt:
    if op == '-n':
        son_number = int(ar)
        print(f'Number of child processes: {son_number}\n')

for i in range(son_number):
    create_child = fork()
    if create_child == 0:
        show_process()