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


## Exercise: Fetch comments of Facebook posts

**Task:** Fetch and export the comments of Facebook posts. 

**Hints:**
1. If you can't fully remember the steps of the fetching process, follow the steps for collecting posts. By now you can skip some steps, such as creating a new database, adding nodes and going through the authentification process.
2. There is a preset to fetch comments. 
3. You can adjust the level for which the query should be executed in the settings section. Manually added seed nodes are on level 1 (e.g. page handle), data queried in the first step can be found on level 2 (so called "child nodes"). You can use the option "Select all nodes" to query all nodes on the selected level simultaniously. 
4. Once you load a preset, the columns change. Make sure to adjust the columns before exporting the data. 

 
