#
# Packages ----
#

import os
from bs4 import BeautifulSoup
import requests
from urllib import parse
import pandas as pd
import re

# For URL parsing...
from urllib.parse import urlparse, urlunparse

# For encoding...
import chardet

# For boilerplate removal...
import trafilatura


#
# Basic scraping functions ----
#

def cleanFilename(url):
    filename = re.sub('[^a-z0-9]', '_', url.lower())
    return filename
    
def downloadUrl(url, directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    
    # Download webpage
    response = requests.get(url)  

    # If status code = 200, download webpage
    if response.status_code == 200:
        with open(directory + '/' + filename, 'wb') as file:
            file.write(response.content)   
            
    return filename


#
# Crawling (extract links) ----
#

def extractLinks(filename, baseurl):
    soup = BeautifulSoup(open(filename, encoding="utf-8"),'lxml')

    links = soup.find_all('a', href=True)    
    links = [link['href'] for link in links]
    links = set(links)                      

    # Add base path to relative URLs
    links = [parse.urljoin(url,link) for link in links]    
    
    return links
    
    
#
# Extract domains ----
#

urlcache = {}
def extractURLparts(url, prefix = ''):
    cachekey = prefix + url
    if not cachekey in urlcache:            
        item = {}

        # Extract domain
        try:
            parsed_uri = urlparse(url)    

            item[prefix+'domain'] = parsed_uri.netloc
            item[prefix+'scheme'] = parsed_uri.scheme
            item[prefix+'path'] = parsed_uri.path
            item[prefix+'params'] = parsed_uri.params
            item[prefix+'query'] = parsed_uri.query
            item[prefix+'fragment'] = parsed_uri.fragment
            
        except Exception as e:
            print(e)
        
        # Normalize domain
        try:
            item[prefix+'domain_normalized'] = re.sub("^www\.","",parsed_uri.netloc).lower()
        except Exception as e:
            print(e)

        urlcache[cachekey] = item
    
    return urlcache[cachekey]

    
 #
 # Boilerplate removal ----
 #
 
 def extractText(filename):
    try:
        with open(filename,'rb') as file:
            txt = file.read()
            encoding = chardet.detect(txt)
            encoding = encoding['encoding'] if encoding['encoding'] is not None else 'utf-8'
            txt = txt.decode(encoding)
    
            txt = trafilatura.extract(txt)
    except Exception as e:
        txt = None
        print(e)
    
    return (txt)


#
# Test functions
#

url = "https://www.aljazeera.com/news/2022/2/24/russia-putin-shatters-peace-europe-ukraine-invasion"

directory = "html"
filename = cleanFilename(url)

downloadUrl(url, directory, filename)

extractURLparts(url)

extractLinks(directory + '/' + filename)

extractText(directory + '/' + filename)