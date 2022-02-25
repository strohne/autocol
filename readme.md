# Workshop Automatic Data Collection

This repository contains materials for the workshop. Before joining the workshop, please prepare yourself acccording to the following steps. In case you struggle with installing the software or packages, don't hesitate to contact us! We are looking forward to the workshop and to letting our computers collect data for us :)  


**Scripts**  
Download the repository by clicking Code -> Download ZIP on the GitHub page. We will update the repository the day before the workshop, please make sure you have the latest version.

**Basic software**
- Download and install the latest version of Facepager (v4.4.3): https://github.com/strohne/Facepager
- Install the browser Firefox and/or Chrome. Optionally, you can install the Chrome Plugin for viewing JSON content: https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh
- Install a text editor with syntax highlighting, for example Notepad++, Atom or Textmate

**Python and Jupyter Lab**  
If you already have a working Jupyter Lab environment, you can skip this step. Otherwise...

- ...download and install Python directly from the webpage https://www.python.org/downloads/ 
- ...open the command prompt / terminal and install Jupyter Lab by calling `pip install jupyterlab`

*Trouble shooting for Windows users:*  Don't miss the step to make Python available in the PATH. If you can't call pip or python from the command prompt, it might be necessary that you first add python and pip to the PATH variable of your computer. Navigate to the file on your computer where python.exe and pip.exe are located and copy the folder path (e.g. C:\Users\Chantal\AppData\Local\Programs\Python\Python310\Scripts). Then edit the environment variables by navigating to Control Panel -> System and Security -> Sytem -> Advanced System Settings -> Environment Variables. Click on the "Path" variable and then click on "Edit" -> "New" and paste your folder path.

Alternatively, you can use a Python-distribution such as Anaconda: https://www.anaconda.com/products/individual.

**Packages**  
During the workshop, we will work with different Python packages. Packages are collections of functions, provided by other developers. 
To install the packages, you can use pip - a package manager that comes with Python. 
You need to open your command prompt / terminal (for example, on Windows press the Windows key and search for "cmd"). In the terminal type the following commands: 

```
pip install os 
pip install requests 
pip install beautifulsoup4
pip install lxml
pip install pandas
pip install matplotlib
pip install seaborn
pip install selenium
```

**Web drivers for selenium**
- Download the latest ChromeDriver for your operating system from https://chromedriver.storage.googleapis.com/index.html?path=99.0.4844.35/
- Download the latest GeckoDriver for your operating system from https://github.com/mozilla/geckodriver/releases

Unzip both ZIP-files and place the files into the folder `4_selenium/drivers`.

         
**Accounts**  
To follow the exercises you will need a Facebook account.



# Schedule

Day 1 - Working with APIs
- 10:00 – 11:30 Introduction to automated data collection.
- 11:30 – 11:45 Break
- 11:45 – 13:00 Practical session: Using APIs with Facepager. 
- 13:00 - 14:00 Lunch break
- 14:00 - 15:15 Practical session: Data wrangling with Python

Day 2 - Webscraping
- 10:00 - 11:30 Introduction to webscrapting
- 11:30 - 11:45 Break
- 11:45 - 13:00 Practical session: Webscraping with Python
- 13:00 - 14:00 Lunch break
- 14:00 - 15:15 Practical session: Webcrawling with Python

Day 3 - Challenges and advanced web scraping techniques
- 9:00 - 10:30 Challenges of automatic data collection
- 10:30 - 11:00 Break
- 11:00 - 12:30 Browser automation using Selenium
- 12:30 - 13:30 Lunch break
- 13:30 - 14:30 Recap and open questions
