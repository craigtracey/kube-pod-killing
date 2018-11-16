import os
import sys
import time


def kill(signal):
    os.kill( os.getpid(), signal )
    print "killed"

if __name__ == '__main__':
    signal = int(sys.argv[1])
    kill(signal)
