import os
import time

start = time.time()

while True:
    delta_time=time.time()-start
    if delta_time>3600:
        os.system('reboot now')
        start = time.time()
    else:
        time.sleep(2)
