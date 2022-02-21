# Data collection with Facepager 

## Workflow to collect posts and comments of a Facebook page

1. **Open Facepager**
2. **New Database:** Create a new database with ```New Database```
3. **Add nodes:** Via ```Add Nodes``` you can add the handle of one or multiple Facebook pages. The handle is the part of the URL after `http://www.facbeook.com/`, e.g. `aljazeera`)
4. **Load preset:** Click the Presets button and load the preset "2. Get Facebook posts" from the Facebook category.  Watch how the settings in the Facebook module changed.
5. **Authentification:** Go through the login dialog after clicking on `Login to Facebook`
6. **Adjust settings:** You can see all available settings in the documentation of the endpoint. The documentation of a resource can be opened via the `?` button next to the resource field. This opens the API Viewer, where you can also find a link to the official documentation. Beware that the documentations of APIs change constantly and that the implemented help may alreay be outdated. 
7. **Fetch data:** Select your node(s) and click on `Fetch Data`
8. **Inspect data:** Expand nodes, review your data in the nodes view (left) and data view (right)
9. **Setup columns:** You can add columns to your nodes view via `Add Column` or `Add All Columns`. Make sure to confirm your selections with `Apply Columns Setup`
10. **Export data:** Select all nodes and click `Export Data` in the menu bar. Choose a name for the file and save it. 

See the export settings below to prepare for the Python excercises.

## Exercise: Fetch comments of Facebook posts

**Task:** Fetch and export the comments of Facebook posts. 

**Hints:**
1. If you can't fully remember the steps of the fetching process, follow the steps for collecting posts. By now you can skip some steps, such as creating a new database, adding nodes and going through the authentification process.
2. There is a preset to fetch comments. 
3. You can adjust the level for which the query should be executed in the settings section. Manually added seed nodes are on level 1 (e.g. page handle), data queried in the first step can be found on level 2 (so called "child nodes"). You can use the option "Select all nodes" to query all nodes on the selected level simultaniously. 
4. Once you load a preset, the columns change. Make sure to adjust the columns before exporting the data. 

 
## Data export

Use the following settings to fetch and export data for the Python excercises:

**Preset:**
Get Facebook posts

**Fields parameter:**
```
message, from, created_time, updated_time,comments.limit(0).summary(1), reactions.limit(0).summary(1), reactions.type(LIKE).limit(0).summary(1).as(like), reactions.type(LOVE).limit(0).summary(1).as(love), reactions.type(HAHA).limit(0).summary(1).as(haha), reactions.type(WOW).limit(0).summary(1).as(wow), reactions.type(SAD).limit(0).summary(1).as(sad), reactions.type(ANGRY).limit(0).summary(1).as(angry), likes.limit(0).summary(true)
```

**Column setup:**  
```
message
from.name
from.id
created_time
updated_time
comments=comments.summary.total_count
reactions=reactions.summary.total_count
likes=like.summary.total_count
love=love.summary.total_count
haha=haha.summary.total_count
wow=wow.summary.total_count
sad=sad.summary.total_count
angry=angry.summary.total_count
```
