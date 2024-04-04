#! python3

# seleniumPractice.py - practicing  with the Selenium web driver module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Read Online")) 
    )
    elem.click()
    # print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
# finally:
#     browser.quit()

# try:
#     elem = browser.find_element_by_tag_name('body')
#     print('Found <%s> element with that class name!' % (elem.tag_name))
# except:
#     print('Was not able to find an element with that name.')