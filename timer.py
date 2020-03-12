import threading
import time
import sys
def countdown(t):
    while t > 0:
        sys.stdout.write('\rDuration : {}s'.format(t))
        t -= 1
        sys.stdout.flush()
        time.sleep(1)

countdown(10)