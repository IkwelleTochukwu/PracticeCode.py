# A Mad libs program that reads in text files and lets the user add their own
# text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
import re, os
RegexPattern = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
def CheckRegex(file_path):
    if os.path.isfile(file_path):
        CheckFile = open(file_path, 'r' )
        CheckContent = CheckFile.read()
        MatchList = RegexPattern.findall(CheckContent)
        for words in MatchList:
             print(input('Enter your ' + words + ' here\n'))
    else:
        print('Invalid file path input')

CheckRegex('C:\\Users\\TOCHUKWU IKWELLE\\Documents\\CLOUD DOCS\\myCLOUD-docs\\testinfile.txt')    # Enter the absolute path of your file here
