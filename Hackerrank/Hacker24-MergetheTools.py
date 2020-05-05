def remove_duplicate(text):
	s = set()
	l = []
	for ch in text:
		if ch not in s:
			s.add(ch)
			l.append(ch)

	return ''.join(l)


def merge_the_tools(string, k):
	iteration = int(len(string)/k)
	start = 0
	end = k
	for i in range(iteration):
		print (remove_duplicate(string[start:end]))
		start = end
		end += k





if __name__ == '__main__':
	string, k = input(), int(input())
	merge_the_tools(string, k)
