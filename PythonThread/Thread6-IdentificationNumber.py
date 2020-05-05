import threading


def do_this():
    x=0
    while x < 500:
        x+=1


def main():

    mythread = threading.Thread(target=do_this)
    mythread.start()
    mythread.join()

    #thread identification.
    print(mythread.ident)

    anotherthread = threading.Thread(target=do_this)
    anotherthread.start()
    print(mythread.ident)
    print(anotherthread.ident)

if __name__ == '__main__':
    main()