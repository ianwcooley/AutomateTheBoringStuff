#! python3

# google.py - do a google search from the command line

import requests, sys, webbrowser
print('Googling...') # display text while downloading the Google page
webbrowser.open('http://google.com/search?q=' + ' '.join(sys.argv[1:]))