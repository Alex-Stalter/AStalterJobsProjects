# Jobs Project
###Author: Alex Stalter
### The following repository is for the COMP490 Senior Design and development at Bridgewater State University.

## Requirements for running.

Please Follow the following Steps.

- In order to run this project you must obtain an api key. You can find the api key registration [here](https://api.data.gov/signup/).
- Make sure to have Python 3.8.7 installed.
- Make sure to include the Requests and Os libraries.
- Create a secrets.py in order to hide the api key. Do not hardcode into URL.

### What the code does.

The following code requests several thousand entries of data from https://api.data.gov/ed/collegescorecard/v1/. In order
accomplish this the program uses the request library to get the information based on the url query and receives the data
JSON format. Each page only has twenty entries the program uses the metadata to find the amount of entries and divide
them by the entries per page which in our case is 20. 

The data received is put into a list called all_data, then the all_data list is sent through a for-loop where it is 
printed line by line into the results.txt file which is created if it does not exist and if it does, it is deleted so 
that the current query can be put into the file.  

### Things to keep in mind while running.

The following project requests over 3,000 entries of data so it will take some time to process.