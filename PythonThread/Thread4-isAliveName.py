import threading

def do_this():
    while True:
        pass

def main():
    mythread = threading.Thread(target=do_this,name='basak')
    mythread.start()

    print(threading.active_count())
    print(threading.enumerate())
    print (mythread.is_alive())

if __name__ == '__main__':
    main()