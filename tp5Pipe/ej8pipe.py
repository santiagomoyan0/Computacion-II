import os
import time
import signal

def handler_father(signal, frame):
    print(f"A (PID={os.getpid()}) reading: ")
    while True:
        line = r.readline()
        if line:
            print(line)
        else:
            pass


def handler_son(signal, frame):
    w.write(f"Mensaje 1 (PID={os.getpid()})\n")
    w.flush()
    os.kill(grandson, signal.SIGUSR1)


def handler_grandson(signal, frame):
    w.write(f"Mensaje 2 (PID={os.getpid()})\n")
    w.flush()
    os.kill(father, signal.SIGUSR2)


father = os.getpid()
r, w = os.pipe()
son = os.fork()
if son != 0:
    os.close(w)
    r = os.fdopen(r)
    signal.signal(signal.SIGUSR2, handler_father)
    time.sleep(1)
    os.kill(son, signal.SIGUSR1)
else:
    grandson = os.fork()
    if grandson != 0:
        os.close(r)
        w = os.fdopen(w, 'w')
        signal.signal(signal.SIGUSR1, handler_son)
    else:
        os.close(r)
        w = os.fdopen(w, 'w')
        signal.signal(signal.SIGUSR1, handler_grandson)
