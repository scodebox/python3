from itertools import product

a = list(input().split())
a = [int(i) for i in a]

b = list(input().split())
b = [int(i) for i in b]

p = list(product(a,b))
for i in p:
	print(str(i)+' ',end='')