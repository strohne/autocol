# Webscraping with Python
# Extract articles from Al Jazeera

# Install packages, if not used before
# pip install os 
# pip install requests 
# pip install beautifulsoup4
# pip install lxml
# pip install pandas


# Load packages
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd


# Set directory and filename for downloads
# (create directory if it doesn't exist yet)
directory = "html"
if not os.path.exists(directory):
    os.makedirs(directory)

   
def cleanFilename(url):
    filename = re.sub('[^a-z0-9]', '_', url.lower())
    return filename
    
def downloadUrl(url, directory, filename):
       
    # Download webpage
    response = requests.get(url)  

    # If status code = 200, download webpage
    if response.status_code == 200:
        with open(directory + '/' + filename, 'wb') as file:
            file.write(response.content)   
            
    return filename

def parseHtml(directory, filename):
    # Parse webpage
    soup = BeautifulSoup(open(directory + '/' + filename, encoding="utf-8"),'lxml')

    # Get all article-elements from soup
    articles = soup.select('article')

    # Initialize empty list for results
    results = []

    for article in articles: 

        # Initialize emty dictionary
        # Extract title and text of articles 
        item = {}
        item['filename'] = filename
        item['title'] = article.select_one('span').text.strip()
        item['text'] = article.select_one('p').text.strip()
        item['url'] = article.select_one('a').get('href')

        # Append items to result-list
        results.append(item)
        
    return results

def parseLinks(directory, filename):
    # Parse webpage
    soup = BeautifulSoup(open(directory + '/' + filename, encoding="utf-8"),'lxml')

    # Get all article-elements from soup
    links = soup.select('a')
    links = [link.get('href') for link in links]
       
    return links
    
    
    
# Searchterms
terms = ['Turkey','China','Germany','USA','Ucraine']
path = "https://www.aljazeera.com/search/"
parameters = "?sort=date"

# Create URLs
urls = [path + term + parameters for term in terms]

# Loop URLs
result = []    

for url in urls:
    filename = cleanFilename(url)
    downloadUrl(url,directory,filename)
    result = result + parseHtml(directory,filename)

# Convert to dataframe
df = pd.DataFrame(result)
display(df)

# Write dataframe to CSV file
df.to_csv('results.csv',sep=";",index=False)
