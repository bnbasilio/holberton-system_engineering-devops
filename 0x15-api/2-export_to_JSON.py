#!/usr/bin/python3
""" 2. Export to JSON """

import json
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

    data = {}
    tasks = []
    for item in jsonResponse:
        tasks.append({"task": item["title"],
                      "completed": item["completed"],
                      "username": USERNAME})
    data = {argv[1]: tasks}

    with open("{}.json".format(argv[1]), 'w') as data_file:
        json.dump(data, data_file)
