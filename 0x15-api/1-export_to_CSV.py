#!/usr/bin/python3
"""TODO list progress"""
from requests import get
from sys import argv
from csv import writer, QUOTE_ALL

if len(argv) > 1:
    userurl = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
else:
    print("Usage: ./0-gather_data_from_an_API.py <userId>")
    exit()
todos = get(userurl + '/todos')
if todos.status_code > 200:
    exit()
todos = todos.json()
user = get(userurl)
if user.status_code > 200:
    exit()
user = user.json()['username']
with open("{}.csv".format(argv[1]), 'w') as myFile:
    myWriter = writer(myFile, quoting=QUOTE_ALL)
    [myWriter.writerow([argv[1], user, task['completed'],
                        task['title']]) for task in todos]
