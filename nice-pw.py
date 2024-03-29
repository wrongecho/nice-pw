#!/usr/bin/env python3

# Project: 		nice-pw
# Date: 		2019-07-20
# Description: 	Generates "nice" passwords in the format of four 
#				dictionary words with two random numbers.
#			    Not intended to be a replacement for secure passwords
#				generated by password managers but provides an easy
#				way to share passwords with others.	

# Note:			I use https://github.com/dwyl/english-words/blob/master/words_alpha.txt
#				And exclude words smaller than 6 characters

import secrets, linecache

def main():
	print("Welcome to the nice password generator\n")
	print("This is not designed to be an alternative to a decent password manager.")
	print("The idea is to generate \"nice\" passwords that can be more easily shared with others (i.e. family).\n")
	
	# //TODO First check dictionary.txt is preset??
	
	# Get total line count and store it in numLines
	numLines = sum(1 for line in open("dictionary.txt", "r"))
	
	# Instantiate the secure SystemRandom class.
	s = secrets.SystemRandom()
	
	# Pick four lines at random to work with
	lineOne = (s.randint(1, numLines))
	lineTwo = (s.randint(1, numLines))
	lineThree = (s.randint(1, numLines))
	lineFour = (s.randint(1, numLines))
		
	# Go to those specific lines and grab the words
	wordOne = linecache.getline("dictionary.txt", lineOne).rstrip("\n").capitalize()
	wordTwo = linecache.getline("dictionary.txt", lineTwo).rstrip("\n").capitalize()
	wordThree = linecache.getline("dictionary.txt", lineThree).rstrip("\n").capitalize()
	wordFour = linecache.getline("dictionary.txt", lineFour).rstrip("\n").capitalize()
	
	# Generate random two digit number
	randDigits = s.randint(10, 99)
	
	# Decide after which word to insert the two random numbers
	numLocation = s.randint(1, 4)
	
	if numLocation == 1:
		randomString = wordOne + str(randDigits) + wordTwo + wordThree + wordFour
	elif numLocation == 2:
		randomString = wordOne + wordTwo + str(randDigits) + wordThree + wordFour
	elif numLocation == 3:
		randomString = wordOne + wordTwo + wordThree + str(randDigits) + wordFour
	else:
		randomString = wordOne + wordTwo + wordThree + wordFour + str(randDigits)
	
	print("Random \"nice\" password:\n")
	print(randomString)
	
	
if __name__ == "__main__":
    main()	