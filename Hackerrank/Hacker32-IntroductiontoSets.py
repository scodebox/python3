def average(array):
    # your code goes here
    s = set(array)
    size = len(s)
    sum = 0
    while len(s):
        sum += s.pop()

    return (sum / size)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
