from collections import defaultdict
#
# d = defaultdict(list)
#
# d['python'].append("Awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print (i)


n,m = [int(x) for x in input().split()]
key=[]

w = defaultdict(list)
for i in range(1,n+1):
    word = input()
    w['n'].append(word)
    # w[word].append(i)

print (w)

for i in range(0,m):
    key.append(input())
# for i in key:
#     positions = w[i]
#     if positions:
#         for p in positions:
#             print (p,end=' ')
#         print ('')
#     else:
#         print(-1)

for i in key:
    if i in w['n']:
        position = 1
        for p in w['n']:
            if i == p:
                print(position,end=' ')
            position+=1
        print('')
    else:
        print(-1)