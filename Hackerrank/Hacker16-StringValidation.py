if __name__ == '__main__':
	s  = input()
	sl = list(s)
	listLen = len(sl)

	for i in range(0,listLen):
		if str(sl[i]).isalnum():
			print (str(sl[i]).isalnum())
			break
		if i == listLen-1:
			print ('False')


	for i in range(0,listLen):
		if str(sl[i]).isalpha():
			print (str(sl[i]).isalpha())
			break
		if i == listLen-1:
			print ('False')


	for i in range(0,listLen):
		if str(sl[i]).isdigit():
			print (str(sl[i]).isdigit())
			break
		if i == listLen-1:
			print ('False')

	for i in range(0,listLen):
		if str(sl[i]).islower():
			print (str(sl[i]).islower())
			break
		if i == listLen-1:
			print ('False')

	for i in range(0,listLen):
		if str(sl[i]).isupper():
			print (str(sl[i]).isupper())
			break
		if i == listLen-1:
			print ('False')