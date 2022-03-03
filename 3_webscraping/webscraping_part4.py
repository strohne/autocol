# Webscraping with Python
# Extract articles from Al Jazeera by using the JSON endpoint


# Load packages
import requests
import json
import urllib.parse
import pandas as pd



# Searchterms
terms = ['Turkey','China','Germany','USA','Ukraine']

# Empty result list
results = []

# Download data
for term in terms:
    print (term)
    for page in range(0,10):
        print(page)
        
        # Assemble URL
        variables = {"query": term, "start": (page * 10) +1,"sort":"date"}
        variables = urllib.parse.quote(json.dumps(variables))
        
        extensions = urllib.parse.quote('{}')

        url = "https://www.aljazeera.com/graphql?wp-site=aje&operationName=SearchQuery&variables="+ variables+"&extensions="+extensions

        # Get data
        response = requests.get(url,headers={'wp-site':'aje'})                  
        data = response.json()
        
        # Extract and prepare data
        items = data['data']['searchPosts']['items']
        
        for item in items:
            item['term'] = term
            results.append(item)
    
    
# Convert to DataFrame
results = pd.DataFrame(results)
results = results.loc[:,['title','link','term']]
display(results)


# Write dataframe to CSV file
results.to_csv('data/articles-fromjson.csv',sep=";",index=False)