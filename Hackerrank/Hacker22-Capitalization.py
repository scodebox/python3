import math
import os
import random
import re
import sys

def scan_index(string):
	if not str.isdigit(string[0]):
		index_list = [0]
	else:
		index_list = []

	for i in range(1,len(string)):
		if string[i-1] == ' ' and string[i] != ' ' and not str.isdigit(string[i]):
			index_list.append(i)

	return index_list

def solve(s):
	index_list = scan_index(s)
	input_string = list(s)
	for i in index_list:
		small = str(input_string[i])
		cap = small.capitalize()
		input_string[i] = cap

	return "".join(input_string)


print(solve('hello   world  lol'))


# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
#
#
# Given a full name, your task is to capitalize the name appropriately.
#
# Input Format
#
# A single line of input containing the full name, .
#
# Constraints
#
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
#
# Output Format
#
# Print the capitalized string, .
#
# Sample Input
#
# chris alan
# Sample Output
#
# Chris Alan