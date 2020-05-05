import threading

def Job():
    print ('Job is goding on.')

def main():

    mythread = threading.Thread(target=Job)
    mythread.start()
    print (threading.active_count())



if __name__ == '__main__':
    main()