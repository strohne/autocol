import re

# Exercise: Extract the date...
text = "https://www.aljazeera.com/news/2021/12/16/what-you-should-know-about-the-conflict-between-russia-ukraine"
re.findall(r"myfancyregex", text)

# Exercise: Extract the search term...
text = "https___www_aljazeera_com_search_turkey"
re.findall(r"myfancyregex", text)

# Load scraped data
import pandas as pd
articles = pd.read_csv("aljazeera-articles-search-facepager.csv", sep=";")
articles


# Extract the date in our scraped data
articles['date']  = articles['link'].str.extract('([0-9]+/[0-9]+/[0-9]+)')

# Drop rows with missing date
articles = articles.dropna()

articles = articles.sort_values(by=['date'])


# Aggregate by day
timeline= articles.groupby(['date','term']).size().to_frame('count')
timeline= timeline.reset_index()
timeline = timeline.sort_values(by=['date'])
timeline


# Plot timeline
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(15,5))
plot = sns.lineplot(x='date', y='count', hue='term', data=timeline)
plot.tick_params(axis='x', rotation=90)