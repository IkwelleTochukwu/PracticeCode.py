#! python3
# StrongPasswordCheck.
import re
StrongPasswordRegex = re.compile(r'[a-z]+[A-Z]+[0-9]+[_\-@*]?')
def StrongPasswordCheck():
    print("Strong password: must contain 'a-z', 'A-Z', '0-9'")
    check = StrongPasswordRegex.search(input('please enter your password\n'))
    if check.group() != None:
        print('SUCESSFUL: Account creation completed')
    else:
        print("Your password is not strong enough! it must contain 'a-z', 'A-Z', '0-9'")

StrongPasswordRegex()


