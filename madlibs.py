# A Mad libs program that reads in text files and lets the user add their own
# text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
# Usage: Enter the absolute path to the text file in the 'CheckRegex()' function call.
import re, os
file_path = 'C:\\Users\\TOCHUKWU IKWELLE\\Documents\\madlibs.txt'    # File path is a variable 
RegexPattern = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
def CheckRegex(file_path):
    if os.path.isfile(file_path):    # Checks if the given path is a valid file in the system disk
        CheckFile = open(file_path, 'r' )
        CheckContent = CheckFile.read()
        MatchList = RegexPattern.findall(CheckContent)
        for words in MatchList:
            values = input('Enter your ' + words + ' here:\n')
            CheckContent = CheckContent.replace(words, values, 1)   # replace the file string with the input string
        print(CheckContent)
    else:
        print('Invalid file path input')

CheckRegex(file_path)    # Enter the absolute path of your file here
                # note that; for Windows OS path, use the '\\' for partioning and '/' for Linux OS
