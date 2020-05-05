from collections import Counter

# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
#
# print (Counter(myList))
#
# print (Counter(myList).items())
#
# print (Counter(myList).keys())
#
# print (Counter(myList).values())


number_of_shoes = input()
# print (number_of_shoes)
size = [int(x) for x in input().split()]
# print (size)
total_customers = int(input())
# print(total_customers)

stock = Counter(size)
profit = 0

for c in range(0, total_customers):
    demand = [int(d) for d in input().split()]
    if stock[demand[0]]:
        stock[demand[0]] = stock[demand[0]] - 1
        profit += demand[1]

print(profit)
