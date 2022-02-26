#
# Import packages ----
#

import pandas as pd
import matplotlib.pyplot as plt  
%matplotlib inline

#
# Load dataset ----
#

df = pd.read_csv("facebooknews.csv", sep=';')

# Show data
display(df)

#
# Select data ----
#

# Select rows
df.loc[df.object_type == 'data',:]
df.loc[(df.object_type == 'data') & (df.level == 1),:]


# Select columns
df.loc[:,['object_id','created_time','comments','reactions','shares','message','from.name']]

# Select rows and columns
df = df.loc[(df.object_type == 'data') & (df.level == 1),['object_id','created_time','comments','reactions','shares','message','from.name']]

#
# Describe data ----
#


# Count posts by author
df.loc[:,'from.name'].value_counts()

# Distribution of the metrics
df.describe()

# Order by comment count to get the post with the most comments
df.sort_values(by=['comments'], ascending=False)

#
# Plots ----
#

# Histogram
df.hist("comments")

# Scatter plot
df.plot.scatter("shares","comments")

# Log scale histogram
plt.hist(df['comments'], log=True)