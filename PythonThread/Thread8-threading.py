import threading
import time
from queue import Queue

print_lock = threading.Lock()

def job(worker):
    time.sleep(0.5)

    with print_lock:
        print (threading.current_thread().name,worker)

#pull an worker from queue and process it
def threader():
    while True:
        #get worker from the queue
        worker = q.get()

        #run the job using worker
        job(worker)

        #complete the job
        q.task_done()

#create an queue and threader
q = Queue()

#how many thread are going to allow in the program
for x in range(10):
    t = threading.Thread(target=threader)
    #classifing the thread as a deamon,so they will die when the main dies
    t.deamon = True
    #begins,
    t.start()


start = time.time()

#20 jobs assigned
for worker in range(20):
    q.put(worker)

#wait until thread terminates
q.join()

#time taken
print ('Entire job took :', time.time()-start)