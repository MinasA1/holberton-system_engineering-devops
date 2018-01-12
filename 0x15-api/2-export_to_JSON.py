#!/usr/bin/python3
"""TODO list progress"""
from requests import get
from sys import argv
from json import dump

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
d = {str(argv[1]): [{'task': t['title'], 'completed': t['completed'],
                     'username': user} for t in todos]}
with open("{}.json".format(argv[1]), 'w') as myFile:
    dump(d, myFile)
