if __name__ == '__main__':
    n = int(input())

    if n % 2 == 1:
        print ('Weird')
    else:
        if n in [2,3,4,5]:
            print ('Not Weird')
        elif n in range(6,21):
            print ('Weird')
        elif n > 20:
            print ('Not Weird')