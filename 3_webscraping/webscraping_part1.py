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
    
filename = directory + "/articles.html"
    
    
# Construct URL from path and searchterm
path = "https://www.aljazeera.com/search/"
searchterm = "Turkey"
url = path + searchterm


# Download webpage
response = requests.get(url)  

# If status code = 200, save webpage
if response.status_code == 200:
    with open(filename, 'wb') as file:
        file.write(response.content)   

        
# Parse webpage
soup = BeautifulSoup(open(filename, encoding="utf-8"),'lxml')


# Get all article-elements from soup
articles = soup.select('article')


# Scrape information from articles

# Initialize empty list for results
results = []

for article in articles: 
    
    # Initialize emty dictionary
    # Extract title and text of articles 
    item = {}
    item['title'] = article.select_one('span').text.strip()
    item['text'] = article.select_one('p').text.strip()
    
    # Append items to result-list
    results.append(item)

    
# Exercise: Scrape the URL of the article. 
# Hint: Goto the documentation https://www.crummy.com/software/BeautifulSoup/bs4/doc/#attributes
# and find out how to get attribute values

# Convert results list to dataframe
results = pd.DataFrame(results)

# Display dataframe
display(results)


# Write dataframe to CSV file
results.to_csv('results.csv',sep=";",index=False)
