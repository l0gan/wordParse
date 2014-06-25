#!/usr/bin/python
# Version 1.3
import sys
from argparse import ArgumentParser
import re
import string
from string import punctuation
import os

parser = ArgumentParser(description='Parse a file for words of a certain length')
parser.add_argument('-f', '--file', default='', help='Dictionary file name.  (Run from directory where dictionary file is located)')
parser.add_argument('-c', '--char_count', default='', help='Number of characters to search for')
parser.add_argument('-b', '--begins', default='', help='FUTURE -  Grab words that begin with a letter or letters')

def main():
	args = parser.parse_args()
	if not len(sys.argv) > 1:
		parser.print_help()
		return
	lines = []
	words = []

	## Get args ##
	filename = args.file
	char_count = args.char_count
	char_count_string = str(char_count)
	
	## Print out filename and char_count ##
	print ('Parsing ' + filename + ' for ' + char_count_string + ' characters')
	
	## New filename is the original filename + char_count ##
	new_file = char_count_string + 'chars_' + filename
	tmp_file = "tmpFile.txt"
	
	## Read in lines from filename ##
	for line in open(filename):
		for word in line.split():
			word = word.rstrip('?.,!;:')
			wordlength = len(word)
			if str(wordlength) == char_count_string:	
				with open(tmp_file, 'a') as f:
					f.write(word + ' ')
					f.close()

	## Sort and Unique ##
	for line in open(tmp_file):
		for word in sorted(set(line.split())):
			with open(new_file, 'a') as f:
				f.write(word + '\n')
				f.close()
	## Remove tmpFile ##
	os.remove(tmp_file)

	print ('Finished!  Check ' + new_file + ' for your new wordlist')

if __name__ == '__main__':
	main()
