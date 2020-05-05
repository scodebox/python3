import threading
def task():
    print ('Job is going on...')
    global dead
    x = 0
    while not dead:
        x+=1
        pass

    print (x)


def main():

    global dead
    dead = False
    t1 = threading.Thread(target=task)
    t1.start()

    print (threading.active_count())
    input('Hit Enter from stop the thread...')
    dead = True
    print ('Thread stopped.')

if __name__ == '__main__':
    main()