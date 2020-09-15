#!/usr/bin/python3
""" 0. Gather data from an API """

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(argv[1]))
    jsonResponse = response.json()
    EMPLOYEE_NAME = jsonResponse["name"]

    response = requests.get(
               'https://jsonplaceholder.typicode.com/todos?userId={}'
               .format(argv[1]))
    jsonResponse = response.json()

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    for task in jsonResponse:
        NUMBER_OF_DONE_TASKS += 1
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks{}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in jsonResponse:
        if task["completed"]:
            print("\t {}".format(task["title"]))
