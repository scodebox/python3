if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    if len(t) == n:
        print (hash(t))