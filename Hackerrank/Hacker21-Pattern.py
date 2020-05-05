def print_rangoli(size):
	first_char = 97
	last_char = (first_char+size)-1
	char_list = []
	while first_char <=last_char:
		char_list.append(chr(first_char))
		first_char+=1

	lines = []
	line = ''
	dash = '--'
	char_list.reverse()
	for i in range(0,size):
		for ch in char_list:
			line = line+ch+'-'
		char_list.reverse()
		char_list.pop(0)
		for ch in char_list:
			line=line+ch+'-'

		char_list.reverse()
		line = line[0:-1]
		if i > 0:
			line = dash+line+dash
			dash+='--'
		lines.append(line)
		line = ''

	lines.reverse()
	for i in lines:
		print(i)
	lines.reverse()
	lines.pop(0)
	for i in lines:
		print(i)



if __name__ == '__main__':
	n = int(input('Enter a number'))
	print_rangoli(n)




