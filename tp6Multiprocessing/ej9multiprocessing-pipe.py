import sys


from multiprocessing import Process, Pipe, current_process

def receptor(conn):
    print("Capturing entrance, use Ctrl + D for exit")
    print("Put text lines :\n")
    sys.stdin = open(0)
    while True:
        try:
            line = input()
            conn.send(line)
        except EOFError:
            print("Exit")
            break


def lector(conn):
    son = current_process().pid
    while True:
        line = conn.recv()
        print(f"Reading (PID={son}): {line}")





if __name__ == "__main__":
    a, b = Pipe()
    process1 = Process(target=receptor, args=(a,))
    process2 = Process(target=lector, args=(b,))
    process1.start()
    process2.start()
    process1.join()
    process2.kill()
