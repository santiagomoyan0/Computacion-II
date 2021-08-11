import os
import signal
import time

def handler_father(signum, frame):
    os.kill(handler2, signal.SIGUSR1)

def handler_child(signum, frame):
    print("I'm the process child n°2 with PID=%d: PONG" % os.getpid())


ret = os.fork()

if ret == 0:
    time.sleep(0.1)
    for i in range(10):
        print("I'm the process n°1 with PID=%d: PING" % os.getpid())
        os.kill(os.getppid(), signal.SIGUSR1)
        time.sleep(5)
else:
    signal.signal(signal.SIGUSR1, handler_father)
    handler2 = os.fork()
    if handler2 == 0:
        signal.signal(signal.SIGUSR1, handler_child)
for i in range(10):
    signal.pause()
