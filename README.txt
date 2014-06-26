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


wordParse - Created by Kirk Hayes (l0gan)

1.  Parse a file for words of a certain length.
2.  Command Line Arguments:
	-f <filename> or --file <filename>  -  'Dictionary file name.  (Run from directory where dictionary file is located)
	-c <number> or --char_count <number>  -  'Number of characters to search for'
	-C <letter or str> or --contains <letter or str>  -  'Grab words that contain a string of characters.  CASE SENSITIVE'
3.  Usage:  python wordParse.py -f sourcefile.txt -c 4 -C the (Search sourcefile.txt for 4 character words that contain the string 'the' and output to output_the_4char_sourcefile.txt)
