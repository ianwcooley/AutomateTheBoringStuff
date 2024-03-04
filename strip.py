#strip.py - function that uses regular expressions to do the
# same thing as the .strip() method

import re

def strip(string):
    stripRegex = re.compile(r'^\s+|\s+$')
    return stripRegex.sub('', string)

print(strip('   \toh     hello world   \n I like trurtles '))