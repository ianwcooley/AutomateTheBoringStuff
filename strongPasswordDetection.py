#! /Library/Frameworks/Python.framework/Versions/3.12/bin/python3
# strongPasswordDetection.py - checks if a password is strong.
# That is, at least 8 characters long, containing both upper and lower case
# letters and at least one digit.

import re

def strongPassword(text):
    strongPasswordRegex = re.compile(r'(([A-Z])|([a-z])|(\d)|.){8,}')
    groups = strongPasswordRegex.search(text)
    if groups == None:
        return False
    if groups.group(2) == None \
    or groups.group(3) == None \
    or groups.group(4) == None:
        return False
    return True 
    
testPasswords = [ \
    'Bouncingbunnies75', \
    '75Bouncingbunnies', \
    'Bouncing75bunnies', \
    'Bouncingbunnies', \
    'BOUNCINGBUNNIES75', \
    'bouncingbunnies75', \
    'Bouncingbunnies&%', \
    '', \
    'abc', \
    'IlikeBouncingBunnies, do you??', \
    '1234567890', \
    '123456B', \
    'bB7', \
    '123456Bb', \
    '12345Bb']

for password in testPasswords:
    if strongPassword(password):
        print(password + ': STRONG')
    else:
        print(password + ': WEAK')
    