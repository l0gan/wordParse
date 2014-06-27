#! /bin/python

# This script will scrape the contents of a given page and save to a file.
# It will then parse the file and scape off the html content.
# Finally it will create a dictionary wordlist from the remaining words on the page that can be used to perform password guessing/cracking.
# For short words like 'it', 'the', 'and', etc. the word list will not save these words.  By specifying the '--concat' option, we will take groups of 3-4 words and create words based on those as well.

# By Kirk Hayes (L0gan)

print '------------------------------------------------------'
print '   _________                                          '
print '   /   _____/ ________________  ______   ___________  '
print '   \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \_  __ \ '
print '   /        \  \___|  | \// __ \|  |_> >  ___/|  | \/ '
print '  /_______  /\___  >__|  (____  /   __/ \___  >__|    '
print '          \/     \/           \/|__|        \/        '
print '------------------------------------------------------'

import sys, os, re, urllib
import urllib2
from bs4 import BeautifulSoup
from argparse import ArgumentParser

parser = ArgumentParser(description='Download the contents of a webpage and scrape the html tags.')
parser.add_argument('-s', '--site', default='', help='Website to scrape')
parser.add_argument('-o', '--output', default='', help='webpage output folder')
parser.add_argument('-d', '--dict', default='YES', help='Also create a dictionary file from webpage contents? (YES or NO) DEFAULT=YES')
parser.add_argument('-c', '--char_count', default='', help='Number of characters to search for - For use with wordParser.py')
parser.add_argument('-C', '--contains', default ='', help='Search for s certain string of characters in the file')


args = parser.parse_args()
if not len(sys.argv) > 1:
	parser.print_help()
site = args.site
output = args.output
dict = args.dict
cleanr = re.compile('<.*?>')
char_count = args.char_count
contains = args.contains

def downSite():
	print ('Scraping ' + site + '.  Please wait.')
	html = urllib2.urlopen(site)
	html = html.read()
	return html


def htmlTagScrape(htmlOut):
	print ('Scraping out HTML tags from ' + site)
	cleantext = re.sub(cleanr,'', htmlOut)
	cleantextFile = "cleantextFile.txt"
	with open(cleantextFile, 'w') as f:
		f.write(cleantext)
		f.close()

def dictCreator(cleantest):
	print ('Calling wordParser.py to create your dictionary.')
	os.system("python wordListParser.py -f cleantextFile.txt" + " -c " + char_count + " -C " +  contains)

def main():
    	if len(sys.argv) < 2 or '-h' in sys.argv or '--help' in sys.argv:
      		sys.exit(help())
	else:
		htmlOut = downSite()
		cleantext = htmlTagScrape(htmlOut)
		if 'YES' in dict or 'yes' in dict:
			dictCreator(cleantext)
		os.remove("cleantextFile.txt")

if __name__ == '__main__':
   main()
