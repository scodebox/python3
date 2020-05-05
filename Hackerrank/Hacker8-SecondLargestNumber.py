if __name__ == '__main__':
	n = int(input())
	arr = [int(x) for x in input().split()]

	arr.sort(reverse=True)
	temp = arr[0]
	for i in arr:
		if temp > i:
			temp =i
			break

	print (temp)