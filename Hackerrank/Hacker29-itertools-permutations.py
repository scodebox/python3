from itertools import permutations

# print (permutations(['1','2','3']))
# print (list(permutations(['1','2','3'])))
# print (list(permutations(['1','2','3'],2)))
# print (list(permutations('abc',2)))

data,r = input().split()
r=int(r)
l=[]
for i in list(permutations(data,r)):
    s=''
    for c in i:
        s+=c.upper()
    l.append(s)
    s=''

for i in sorted(l):
    print(i)
