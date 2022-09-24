#! python3
# StrongPasswordCheck.
''' A function that uses regex to make sure the password string it is passed through user
user input, is strong enough. A strong password is defined as one that is at 
least eight characters long, contains both uppercase and lowercase characters, and has at least one digit'''

import re
StrongPasswordRegex = re.compile(r'[a-z]+[A-Z]+[0-9]+')  # A bug which only allows for strong passwords
                                                         # that are written in precedence following the regex 
def StrongPasswordCheck():
    print("Strong password: must contain 'a-z', 'A-Z', '0-9'")
    password = input('password must be at least 8 characters long\n')
    if len(password) >= 8:
        check = StrongPasswordRegex.search(password)
        if check != None:
            print('SUCCESSFUL: Password registered')
        elif check == None:
            print("Your password is not strong enough! it must contain 'a-z', 'A-Z', '0-9'")
    elif len(password) < 8:
        print('password must be at least 8 characters long')

StrongPasswordCheck()


