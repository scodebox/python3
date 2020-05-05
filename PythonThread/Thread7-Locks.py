import threading

def do_this():
    global x,lock

    lock.acquire()
    try:
        while x < 3000:
            x+=1
        print (x)
    finally:
        lock.release()

def Now_do_this():
    global x, lock
    lock.acquire()
    try:
        x=1500
        while x < 6000:
            x+=1
        print (x)
    finally:
        lock.release()

def main():
    global x,lock
    x = 0

    lock = threading.Lock()
    t1 = threading.Thread(target=do_this)
    t2 = threading.Thread(target=Now_do_this)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
