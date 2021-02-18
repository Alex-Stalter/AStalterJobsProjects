# Jobs Project
### Author: Alex Stalter
### The following repository is for the COMP490 Senior Design and development at Bridgewater State University.

## Requirements for running.

Please do the following.

- In order to run this project you must obtain an api key. You can find the api key registration [here](https://api.data.gov/signup/).
- Make sure to have Python 3.8.7 installed.
- The git does not include a virtual environment so make sure to create your own using pycharm.   
- Make sure the Requests and Os libraries are working and installed properly.
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

### Tests
Currently, two tests are being run, the first test checks to make sure that over 1000 entries were retrieved from
the website. The second test creates a sample database with a sample school to make sure that 
the database functions inside the program are working correctly.

### Things to keep in mind while running.

The following project requests over 3,000 entries of data so it will take some time to process.

## Database Structure
The database created in the code, which is named jobs_db.sqlite, is currently a single table with seven columns each
corresponding to one of the seven values retrieved through the government data website. The primary key of the table is 
the school id which is a unique number that is pulled from the university data website.