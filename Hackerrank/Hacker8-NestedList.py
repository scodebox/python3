if __name__ == '__main__':
	result = []
	gradeList = []
	for _ in range(int(input())):
		newList = []
		name = input()
		score = float(input())
		gradeList.append(score)
		newList.append(name)
		newList.append(score)

		result.append(newList)

	gradeList.sort()
	for i in range(0,len(gradeList)-1):
		if gradeList[i] != gradeList[i+1]:
			secondLow = gradeList[i+1]
			break

	result.sort()
	for student in result:
		if student[1] == secondLow:
			print (student[0])
