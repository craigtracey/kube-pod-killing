import os
import sys


def kill(signal):
    os.kill( os.getppid(), signal )

if __name__ == '__main__':
    signal = int(sys.argv[1])
    kill(signal)
