# Selenium package to remote control the browser
from selenium import webdriver 
from selenium.webdriver.common.by import By


# Driver for Chrome browser
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#chrome_service = Service(ChromeDriverManager().install())

# Driver for Firefox browser
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

firefox_service = Service(GeckoDriverManager().install())


#
# Open browser
#


# For chrome
#browser = webdriver.Chrome(service=chrome_service)

# For Firefox
browser = webdriver.Firefox(service=firefox_service)

# Open page
browser.get("https://www.google.com/")

# Wait up to 10 seconds when using elements,
# needed because elements are only accessible when page has been loaded
browser.implicitly_wait(10)

# Find search input
# See the documentation: https://selenium-python.readthedocs.io/locating-elements.html
input_search = browser.find_element(By.NAME,"q")

# Type into the search input
input_search.send_keys("How to find ")

# Submit
input_search.submit()


#
#  Extract data 
#

# Get number of search results
results = browser.find_element(By.ID,'result-stats')
print(results.text)


# Extract number of search results
import re
number = re.search('([0-9\.]+) Ergebnisse',  results.text).group(1)

# Remove dot from text 
number = number.replace('.','')

# Convert to integer number (int)
number = int(number)
print(number)

#
# Multiple searches
#

# URL und keyword list for multiple search terms
url = "https://www.google.com/"
keywords = ["Computational","Statistical","Interpretive"]

# Empty list for search results
results = []

# Google every search term,
# extract the number,
# and add them to the results list 

for keyword in keywords:
    print(keyword)    
    browser.get(url)
    
    input_search = browser.find_element(By.NAME,"q")
    input_search.send_keys(keyword)
    input_search.submit()    
    
    number = browser.find_element(By.ID,'result-stats').text
    results.append({'keyword':keyword, 'count':number })


import pandas as pd

pd.DataFrame(results)