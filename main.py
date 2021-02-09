# Author: Alex Stalter

import requests
import secrets
import os

# format_url() uses a hardcoded url and adds the queries to it so that it is easier to manage and to read.


def format_url():
    query = ["school.name", "school.state", "2018.student.size", "2017.student.size",
             "2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line",
             "2016.repayment.3_yr_repayment.overall"]
    sort = query[4]
    degree_type = "school.degrees_awarded.predominant=2,3"
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?"+degree_type + "&fields=id"
    for x in query:

        url += "," + x
    url += "&sort=" + sort

    return url
# get_data takes the inputted URL and adds the api_key from secrets.py to the end of the url.
# the function then loops through all of the pages given the information from the metadata.
# looks good demo comment for checking actions


def get_data(url: str):
    # TODO: general clean up to make code more readable.
    all_data = []
    full_url = f"{url}&api_key={secrets.api_key}"
    response = requests.get(full_url)
    if response.status_code != 200:
        print(response.text)
        return []
    json_data = response.json()
    metadata = json_data['metadata']
    total_data = metadata['total']
    per_page = metadata['per_page']
    pages = round(total_data/per_page)

    for x in range(pages+1):
        response = requests.get(full_url)
        if response.status_code != 200:
            print(response.text)
            return[]
        json_data = response.json()
        results = json_data['results']
        all_data.extend(results)
        full_url = f"{url}&api_key={secrets.api_key}&page={x+1}"

    write_to_file(all_data, "raw_results.txt")
    write_to_file(clean_data(all_data), "clean_results.txt")
# clean_data() takes in the raw data taken from the results and formats it to be more readable.


def clean_data(unclean_data):
    cleaned_data = []
    for x in unclean_data:
        name = x['school.name']
        state = x['school.state']
        school_id = x['id']
        a_size = x['2017.student.size']
        b_size = x['2018.student.size']
        earnings = x['2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line']
        repayment = x['2016.repayment.3_yr_repayment.overall']
        cleaned_data.append((f"school.name:{name},school.state:{state},id:{school_id},2017.size:{a_size},"
                            f"2018.size:{b_size},earning:{earnings},repayment:{repayment}"))

    return cleaned_data
# write_to_file() takes in data and a file in the form of a string in order to create a file to write the data to.


def write_to_file(data, file: str):

    if os.path.exists(file):
        os.remove(file)
    results_file = open(file, 'x')
    for x in data:
        results_file.write(str(x))
        results_file.write("\n")
    results_file.close()
# main() starts the program.


def main():
    get_data(format_url())


if __name__ == '__main__':
    main()
