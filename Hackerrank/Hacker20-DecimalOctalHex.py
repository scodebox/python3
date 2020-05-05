def print_formatted(number):
	for i in range(1, number + 1):
		octal = oct(i)[2:]
		hexadecimal = hex(i)[2:].upper()
		binary = bin(i)[2:]
		if number == 2:
			print ("%2d %2s %2s %2s" % (i,octal,hexadecimal,binary))
		if number == 17:
			print ("%5d %5s %5s %5s" % (i,octal,hexadecimal,binary))
		if number == 99:
			print ("%7d %7s %7s %7s" % (i,octal,hexadecimal,binary))
		if number == 63:
			print ("%6d %6s %6s %6s" % (i,octal,hexadecimal,binary))


if __name__ == '__main__':
	n = int(input())
	print_formatted(n)




# Given an integer, , print the following values for each integer  from  to :
#
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of .
#
# Input Format
#
# A single integer denoting .
#
# Constraints
#
# Output Format
#
# Print  lines where each line  (in the range ) contains the respective decimal, octal, capitalized hexadecimal, and binary values of . Each printed value must be formatted to the width of the binary value of .
#
# Sample Input
#
# 17
# Sample Output
#
#     1     1     1     1
#     2     2     2    10
#     3     3     3    11
#     4     4     4   100
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8    10     8  1000
#     9    11     9  1001
#    10    12     A  1010
#    11    13     B  1011
#    12    14     C  1100
#    13    15     D  1101
#    14    16     E  1110
#    15    17     F  1111
#    16    20    10 10000
#    17    21    11 10001
