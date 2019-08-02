#!/usr/bin/env python3

# Project: 		nice-pw/prep-dictionary
# Date: 		2019-07-20

# Description: 	Simply exclude words smaller than 5
#				characters from words_alpha.txt
#				and outputs remaining to dictionary.txt

alphafile = open("input.txt", "r")
cleaner = open("dictionary.txt", "w+")
for line in alphafile:
	line.rstrip("\n")
	if len(line) > 5:
		cleaner.write(line)