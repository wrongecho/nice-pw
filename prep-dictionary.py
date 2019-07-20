#!/usr/bin/env python3

# Project: 		nice-pw/prep-dictionary
# Date: 		2019-07-20

# Description: 	Simply exclude words smaller than 6
#				characters from words_alpha.txt
#				and outputs remaining to dictionary.txt

alphafile = open("words_alpha.txt", "r")
cleaner = open("dictionary.txt", "w+")
for line in alphafile:
	line.rstrip("\n")
	if len(line) > 6:
		cleaner.write(line)