#! python3

# wikiImages.py - Searches Wikipedia for a topic, and if it finds
# a page on the topic, downloads all photos on that page.
# Usage:
#   ./wikiImages.py <search terms>

import sys, os, webbrowser, re, requests, bs4
from selenium import webdriver
from selenium.webdriver.common.by import By

# find page if it exists
searchTerms = ' '.join(sys.argv[1:])
driver = webdriver.Chrome()
driver.get('http://wikipedia.org')
searchInput = driver.find_element(By.ID, 'searchInput')
searchInput.send_keys(searchTerms)
searchInput.submit()
url = driver.current_url
driver.quit()

# If url contains '/wiki/' this seems to indicate that the page exists,
# or at the very least a disambiguation page.
if re.search('/wiki/', url):
    
    # Store files in a directory named based on search terms.
    dirName = '_'.join(sys.argv[1:])
    os.makedirs(dirName, exist_ok=True)
    
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    # Find all images on the page
    images = soup.find_all('img')
    print('Downloading images...')
    for image in images:
        imageURL = 'https:' + image.get('src')
        # Download images
        try:
            res = requests.get(imageURL)
            res.raise_for_status()
            imageFile = open(os.path.join(dirName, os.path.basename(imageURL)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        except Exception as error:
            print(f"An error occurred: {error}")
else:
    print('No page found.')
