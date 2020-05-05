def welcome(width):
	text = 'WELCOME'
	dash_len = width - len(text)
	print ('-'*int(dash_len/2) + text + '-'*int(dash_len/2))

height, width = input().split()
width = int(width)
half_height = int(int(height)/2)

design = '.|.'
design_counter = 1
design_list = []
for i in range(1,half_height+1):
	no_of_dash = width - (design_counter*len(design))
	no_of_dash_in_each_side = int(no_of_dash/2)

	current_line = '-'*no_of_dash_in_each_side + design*design_counter + '-'*no_of_dash_in_each_side
	design_list.append(current_line)
	print (current_line)
	design_counter+=2

welcome(width)
design_list.reverse()
for i in design_list:
	print (i)

# Mr.Vincent
# works in a
# door
# mat
# manufacturing
# company.One
# day, he
# designed
# a
# new
# door
# mat
# with the following specifications:
#
# Mat
# size
# must
# be
# X.( is an
# odd
# natural
# number, and is times.)
# The
# design
# should
# have
# 'WELCOME'
# written in the
# center.
# The
# design
# pattern
# should
# only
# use |,.and - characters.
# Sample
# Designs
#
# Size: 7
# x
# 21
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME - ------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
#
# Size: 11
# x
# 33
# ---------------.|.---------------
# ------------.|..|..|.------------
# ---------.|..|..|..|..|.---------
# ------.|..|..|..|..|..|..|.------
# ---.|..|..|..|..|..|..|..|..|.---
# -------------WELCOME - ------------
# ---.|..|..|..|..|..|..|..|..|.---
# ------.|..|..|..|..|..|..|.------
# ---------.|..|..|..|..|.---------
# ------------.|..|..|.------------
# ---------------.|.---------------
