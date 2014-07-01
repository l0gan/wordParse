@@@        @@@@@@@@    @@@@@@@@   @@@@@@   @@@  @@@  
@@@       @@@@@@@@@@  @@@@@@@@@  @@@@@@@@  @@@@ @@@  
@@!       @@!   @@@@  !@@        @@!  @@@  @@!@!@@@  
!@!       !@!  @!@!@  !@!        !@!  @!@  !@!!@!@!  
@!!       @!@ @! !@!  !@! @!@!@  @!@!@!@!  @!@ !!@!  
!!!       !@!!!  !!!  !!! !!@!!  !!!@!!!!  !@!  !!!  
!!:       !!:!   !!!  :!!   !!:  !!:  !!!  !!:  !!!  
 :!:      :!:    !:!  :!:   !::  :!:  !:!  :!:  !:!  
 :: ::::  ::::::: ::   ::: ::::  ::   :::   ::   ::  
: :: : :   : : :  :    :: :: :    :   : :  ::    :   


scraper - Created by Kirk Hayes (l0gan)

1.  Scrape the contents of a website
2.  Command Line Arguments:
	-s <site> or --site <site> - Website to scrape.  (must put in http:// or https://)
	-d <YES or NO> or --dict < YES or NO> - Create Dictionary file from page contents? (Default = YES) - This will pass the website contents to wordParser
	-c <number> or --char_count <number> - Number of characters to search for (for passing to wordParser)
        -C <letter or str> or --contains <letter or str>  -  Grab words that contain a string of characters.  CASE SENSITIVE (for passing to wordParser)
3.  Usage:  
	python scraper.py -s http://website.com -d YES -c 5 -C the 
(Scrape contents of http://website.com then create a dictionary file of words 5 characters and contain the string 'the'.  Will output to output_the_5char_cleantextFile.txt.)


wordParser - Created by Kirk Hayes (l0gan)

1.  Parse a file for words of a certain length.
2.  Command Line Arguments:
	-f <filename> or --file <filename>  -  'Dictionary file name.  (Run from directory where dictionary file is located)
	-c <number> or --char_count <number>  -  'Number of characters to search for'
	-C <letter or str> or --contains <letter or str>  -  'Grab words that contain a string of characters.  CASE SENSITIVE'
3.  Usage:  
	python wordParse.py -f sourcefile.txt -c 4 -C the 
(Search sourcefile.txt for 4 character words that contain the string 'the' and output to output_the_4char_sourcefile.txt)
