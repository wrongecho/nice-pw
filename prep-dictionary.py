#!/usr/bin/env python3

alphafile = open("words_alpha.txt", "r")
cleaner = open("dictionary.txt", "w+")
for line in alphafile:
	line.rstrip("\n")
	if len(line) > 6:
		cleaner.write(line)