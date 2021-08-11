import os
import getopt
import sys
import signal
import time

def handler_child(s, f):
    print(f" I'm the PID: {os.getpid()}, receive the signal {s} from my father PID {os.getppid()}")
    os._exit(0)

def father(childs):
    signal.signal(signal.SIGUSR2, signal.SIG_IGN)

    for i in range(childs):
        ret = os.fork()
        if ret == 0:
            signal.signal(signal.SIGUSR2, handler_child)
            signal.pause()
        else:
            print("building the process:", ret)
            time.sleep(0.1)
            os.kill(ret, signal.SIGUSR2)

childs = 0

(opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['process='])

for (op, ar) in opt:
        if (op in ['-p', '--process']):
            if (childs == 0):
                childs = int(ar)
            else:
                sys.exit(2)

father(childs)
