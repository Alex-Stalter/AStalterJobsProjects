# Jobs Project
### Author: Alex Stalter
### The following repository is for the COMP490 Senior Design and development at Bridgewater State University.

## Requirements for running.

Please do the following.

- In order to run this project you must obtain an api key. You can find the api key registration [here](https://api.data.gov/signup/).
- Make sure to have Python 3.8.7 installed.
- The git does not include a virtual environment so make sure to create your own using pycharm.   
- Make sure the Requests, Os, pandas, openpyxl, plotly, and pyside6 libraries are working and installed properly.
- Create a secrets.py in order to hide the api key. Do not hardcode into URL.

## What the code does.

To start off a database is created called jobs_db where all the data will be put into. One table is currently created 
called school and 7 columns are created to hold the data that is requested from the government data site.

The following code then requests several thousand entries of data from https://api.data.gov/ed/collegescorecard/v1/. In order 
to accomplish this the program uses the request library to get the information based on the url query and receives the data
JSON format. Each page only has twenty entries the program uses the metadata to find the amount of entries and divide
them by the entries per page which in our case is 20. 

The data received is put into a list called all_data, then the all_data list is sent through the insert_data() function
where it is put into the database created called jobs_db. 

The program also reads in data on jobs by state in from an Excel spreadsheet that is in the project directory. The data 
from the spreadsheet is formatted into a dictionary adn then inserted into a new table that is called Jobs.

The function that inserts the school data into the Database also handles the data from teh jobs database.

In addition to the above the following data is also displayed in a GUI that is displayed below.

### Tests

Four tests are run to make sure each element of the program works flawlessly.

The first test is a very simple test that looks at the data retrieved from online and makes sure that there are more
than 1000 entries that come in.

The second test checks to make sure that the database opens and has two tables in it. Once the test database has been
sample data is created to pass into the database and then a query is run to make sure that any data that is put into the 
database can be correctly accessed and nothing happens to the data when it is passed in. 

The third test checks on the Excel functions of the program to make sure that the data from the spreadsheet that is
being used in the program is getting more than 1000 items and is getting data from all fifty states. In this case the
extra 4 territories are also included.

The fourth test creates sample data that is first input into a sample Excel file and then sent through the excel_import()
function where it returns the data as a dictionary and then that dictionary is passed into the function to put the data 
into a sample database. A simple query is then run on the database and compared against the original list to make sure
the data is not changed along the way and can be accessed correctly.

### Things to keep in mind while running.

The following project requests over 3,000 entries of data so it will take some time to process and will print out
a message once getting the school data and excel data has finished.

## Database Structure

The database created in the code, which is named jobs_db.sqlite, is currently a two table database the first is school 
which has with seven columns each corresponding to one of the seven values retrieved through the government data website
. The primary key of the table is the school id which is a unique number that is pulled from the university data website
. The second table is called Jobs and is filled with data from an Excel spreadsheet which a report of jobs from 2019
. The Jobs table consists of six columns id, state, occupation code, title, employment, and salary. There is a third 
table which allows the two previous tables to be linked together with a many ot many relationship.

##GUI


The gui does two things firstly it allows the user to import extra data into the database and also replace current
elements in the database using excel files. The second function allows the user to visualize the data in two ratios
firstly the ration of graduates to toal employment nad secondly the ratio of Declining loan balance and average entry
salary.

###Things to keep in mind while using the GUI.


You can only edit information from one table at a time and also only by one way at a time either through excel
or individual entries using the UI. In order for them to work the other must be empty. Also keep in mind
the data in your excel sheet must be the same format as the data you would enter into the UI.

For the map visualization the text visualization just make sure to select how you would like to see the data or else it 
will display a default data of ordering the text by state name alphabetically, and the graduates per state for the map.