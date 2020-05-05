import threading

def do_first():
    global x
    while x < 300:
        x+=1

    print (x)

def do_second():
    global x
    while x < 600:
        x+=1
    print (x)

def main():
    global x
    x = 0
    t1 = threading.Thread(target=do_first)
    t1.start()
    t1.join()

    t2 = threading.Thread(target=do_second)
    t2.start()

if __name__ == '__main__':
    main()