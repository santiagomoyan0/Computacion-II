from os import getpid, fork, wait

def 5_son():
    for i in range(5):
        print(f'Im the son, PID: {getpid()}')

son = fork()

if son:
    id_process = getpid()
    print(f'Im the father , PID: {id_process}, my son is: {son}')
    print(f'Im the father, PID: {id_process}, my son is: {son}')
    wait()
    print(f'My child process, PID: {son} finished')
else:
    5_son()
    print(f'Son PID: {getpid()}, finished')

