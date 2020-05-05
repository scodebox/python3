def sum_checker(n):
    sq = str(n**2)
    total_len = int(len(sq))
    half_len = int(len(sq)/2)
    if half_len > 1 and (int(sq[:half_len])+int(sq[half_len:]) == n or int(sq[:half_len+1])+int(sq[half_len+1:]) == n or int(sq[:half_len-1])+int(sq[half_len-1:]) == n):
        print(n, ' Kaprekar Number D')
        return
    for i in range(half_len+1):
        a, b = int(sq[:i] or 0), int(sq[i:])
        c, d = int(sq[:total_len-i]), int(sq[total_len-i:] or 0)
        if a and d and (a+b == n or c+d == n):
            print(n, ' Kaprekar Number')
            return


start = int(input('START :: '))
end = int(input('END :: '))
for i in range(start,end+1):
    sum_checker(i)

print('\nDone')
input()