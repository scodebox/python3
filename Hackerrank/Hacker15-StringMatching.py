def count_substring(string, sub_string):
	count = 0
	stringList = list(string)
	sub_stringList = list(sub_string)

	for i in range(0,len(stringList)):
		if string[i:i+len(sub_stringList)] == sub_string:
			count+=1
	return count


if __name__ == '__main__':
	string = input().strip()
	sub_string = input().strip()

	count = count_substring(string, sub_string)
	print(count)