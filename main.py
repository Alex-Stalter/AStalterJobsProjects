# Author: Alex Stalter

import requests
import secrets
import os

# get_data takes the inputted URL and adds the api_key from secrets.py to the end of the url.
# the function then loops through all of the pages given the information from the metadata.


def get_data(url: str):
    # TODO: general clean up to make code more readable.
    all_data = []
    full_url = f"{url}&api_key={secrets.api_key}"
    response = requests.get(full_url)
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

    return all_data


def write_to_file(data):
    # TODO: Clean up results so that the file does not include unneeded things. Such as brackets and extra long labels.
    if os.path.exists("results.txt"):
        os.remove("results.txt")
    results_file = open("results.txt", 'x')
    for x in data:
        results_file.write(str(x))
        results_file.write("\n")
    results_file.close()


def main():
    # TODO: Clean up url so that it is easier to read and manage.
    # The URL query gets all of the minimum required data and sorts by earnings.

    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&" \
          "fields=id,school.state,school.name,2018.student.size,2017.student.size," \
          "2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2016.repayment.3_yr_repayment.overall" \
          "&sort=2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line"
    all_data = get_data(url)
    write_to_file(all_data)


if __name__ == '__main__':
    main()
