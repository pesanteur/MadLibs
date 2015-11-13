#! /usr/bin/env python3
#  mlg.py - Reads in text files and lets the user add own text.
#  Usage: python mlg.py <filename> 
#  test file is madlibs.txt

import sys, re, string

#TODO: Opens and Reads in text files 
filename = sys.argv[1].lower()
openfile = open('/Users/Pesanteur/Desktop/Python/%s.txt' % filename, 'r')
readfile = openfile.read()

#TODO: Find words ADJECTIVE, NOUN, ADVERB or VERB
wordsplit = readfile.split()
for word in wordsplit:
	word = word.strip(string.punctuation)
	if word == "ADJECTIVE":
		adjinput = str(raw_input("Enter an adjective:\n"))
		adjRegex = re.compile(r'ADJECTIVE')
		readfile = adjRegex.sub(adjinput, readfile, count = 1)
	if word == "NOUN":
		nouninput = str(raw_input("Enter a noun:\n")) 	
		nounRegex = re.compile(r'NOUN')
		readfile = nounRegex.sub(nouninput, readfile, count = 1)
 	if word == "VERB":
		verbinput = str(raw_input("Enter a verb:\n"))
		verbRegex = re.compile(r'VERB')
		readfile = verbRegex.sub(verbinput, readfile, count = 1) 

closefile 

print readfile	
