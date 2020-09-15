#!/usr/bin/python3
""" 1. Export to CSV """

import csv
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))
    jsonResponse = response.json()
    USERNAME = jsonResponse["username"]

    response = requests.get(
               'https://jsonplaceholder.typicode.com/todos?userId={}'
               .format(argv[1]))
    jsonResponse = response.json()

    with open("{}.csv".format(argv[1]), 'w') as data_file:
        csv_writer = csv.writer(data_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in jsonResponse:
            csv_writer.writerow([argv[1], USERNAME, task["completed"],
                                task["title"]])
