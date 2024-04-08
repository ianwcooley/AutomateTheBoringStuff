#! python3

# wikipedia.py - search wikipedia for a topic
# Usage:
#   ./wikipedia.py <search terms>

import sys, webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By

searchTerms = ' '.join(sys.argv[1:])
driver = webdriver.Chrome()
driver.get('http://wikipedia.org')
searchInput = driver.find_element(By.ID, 'searchInput')
searchInput.send_keys(searchTerms)
searchInput.submit()
url = driver.current_url
driver.quit()
webbrowser.open(url)
