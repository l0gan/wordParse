#!/usr/bin/python
# Version 1.5
import sys
from argparse import ArgumentParser
import re
import string
from string import punctuation
import os

parser = ArgumentParser(description='Parse a file for words of a certain length')
parser.add_argument('-f', '--file', default='', help='Dictionary file name.  (Run from directory where dictionary file is located)')
parser.add_argument('-c', '--char_count', default='', help='Number of characters to search for')
parser.add_argument('-C', '--contains', default='', help='Grab words that contain a string of characters.  CASE SENSITIVE')

args = parser.parse_args()
if not len(sys.argv) > 1:
	parser.print_help()


## Variables ##
filename = args.file
char_count = args.char_count
char_count_string = str(char_count)
contains = args.contains
new_file = 'output_' + contains + '_' + char_count_string + 'chars_' + filename
tmp_file = "tmpFile.txt"
tmp_file2 = "tmpFile2.txt"

def character_counter():
	 for line in open(filename):
                for word in line.split():
                        word = word.rstrip('?.,!;:')
                        wordlength = len(word)
                        if str(wordlength) == char_count_string:
                                with open(tmp_file, 'a') as f:
                                        f.write(word + ' ')
                                        f.close()

def containing():
	if len(char_count_string) > 0:
		cont_file = tmp_file
	else:
		cont_file = filename
	for line in open(cont_file):
               	for word in line.split():
                       	word = word.rstrip('?.,!;:')
                       	wordcont = str(contains)
                       	if wordcont in word:
                               	with open(tmp_file2, 'a') as f:
                                       	f.write(word + ' ')
                                       	f.close()
 

def sorter():
## Sort and Unique ##
	if len(contains) > 1:
		sort_file = tmp_file2
		try:
			srt_file = open(sort_file)
		except IOError:
			print ('No words found that matched the string ' + str(contains))
			exit()
	elif len(char_count_string) > 0:
		sort_file = tmp_file
	else:
		parser.print_help()
		exit()
	for line in open(sort_file):
                for word in sorted(set(line.split())):
                        with open(new_file, 'a') as f:
                                f.write(word + '\n')
                                f.close()
        ## Remove tmpFile ##
	os.remove(sort_file)


def main():
        lines = []
        words = []

        ## Print out filename and char_count ##
        print ('Parsing ' + filename + ' for ' + char_count_string + ' characters')

        if len(char_count_string) > 0:
                character_counter()

        if len(contains) > 1:
                containing()

        sorter()

        print ('Finished!  Check ' + new_file + ' for your new wordlist')



if __name__ == '__main__':
	main()
