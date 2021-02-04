import requests
import secrets


def get_data(url: str):
    all_data = []
    full_url = f"{url}&api_key={secrets.api_key}"
    response = requests.get(full_url)
    json_data = response.json()
    metadata = json_data['metadata']
    total_data = metadata['total']
    per_page = metadata['per_page']
    pages = round(total_data/per_page)

    for x in range(pages):
        response = requests.get(full_url)
        if response.status_code != 200:
            print(response.text)
            return[]
        json_data = response.json()
        results = json_data['results']
        all_data.extend(results)
        full_url = f"{url}&api_key={secrets.api_key}&page={x+1}"

    return all_data


def main():
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&" \
          "fields=id,school.state,school.name,2018.student.size,2017.student.size," \
          "2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2016.repayment.3_yr_repayment.overall"
    all_data = get_data(url)
    for x in all_data:
        print(x)


if __name__ == '__main__':
    main()
