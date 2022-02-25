# Exercise: Extract the date...

import re

text = "https://www.aljazeera.com/news/2021/12/16/what-you-should-know-about-the-conflict-between-russia-ukraine"
re.findall(r"[0-9]+/[0-9]+/[0-9]+", text)

# Exercise: Extract the search term...


text = "https___www_aljazeera_com_search_turkey"
re.findall(r"[a-z]+$", text)


# Load scraped data
import pandas as pd
articles = pd.read_csv("data/articles-search.csv", sep=";")
articles

# Extract the date in our scraped data

articles['date']  = articles['url'].str.extract('([0-9]+/[0-9]+/[0-9]+)')

# Convert to datetime object
articles['date'] = pd.to_datetime(articles['date'], dayfirst=False)

# Construct month string
articles['month'] = articles['date'].dt.strftime('%Y-%m')

# Drop rows with missing date
articles = articles.dropna()

articles = articles.sort_values(by=['date'])


# Extract search term

articles['term'] = articles['filename'].str.extract('([^_]+$)')

articles

# Aggregate by month

timeline= articles.groupby(['month','term']).size().to_frame('count')
timeline= timeline.reset_index()
timeline = timeline.sort_values(by=['month'])
timeline


# Plot timeline
import seaborn as sns

plot = sns.lineplot(x='month', y='count', hue='term', data=timeline)
plot.tick_params(axis='x', rotation=90)