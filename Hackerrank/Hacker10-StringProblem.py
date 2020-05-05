'''
Input
-----
You are given a single line of text, with length at most 1000
characters. The text consists of English words. Adjacent words in the
line are separated by a single space.

The second line consists of a single integer 'N' denoting the width of
an output line.

Output 
-----
Print the input text in the following format: 
1. no line of output must be more than N characters long.
2. no word can be split across two lines. If a word does not
   completely fit in a line, move the word to the next line.

Sample Input
------------
O SOFT embalmer of the still midnight Shutting with careful fingers 
34

Sample Output
-------------
O SOFT embalmer of the still 
midnight Shutting with careful 
fingers

Explanation
-----------
Each output line is at most 34 characters long. "midnight" does not
fit on the first line, hence it was moved to the second
line. "fingers" does not fit on the second line, hence it was moved
to the third line.
'''

text = input('\nEnter Text :: ')
lineLength = int(input('Enter width :: '))

print('\nOUTPUT ::\n')

wordList = text.split(' ')
line = []
currentLength = 0
flag = 0

for word in wordList:
	if flag == 0:
		line.append(word)
		currentLength += len(word)
		flag = 1
	elif flag == 1:
		line.append(' ')
		line.append(word)
		currentLength += len(' ' + word)
	if currentLength >= lineLength:
		subText = ''
		for lineWord in line[0:len(line) - 2]:
			subText += lineWord
		print(subText)

		currentLength = len(line[-1])
		line = [line[-1]]
print(line[0])

print('\n' * 3)
