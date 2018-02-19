#!/usr/bin/python3
"""Employees Todo tasks list"""
from sys import argv
from json import dump
from requests import get
if __name__ == "__main__":
    userurl = 'https://jsonplaceholder.typicode.com/users'
    todourl = 'https://jsonplaceholder.typicode.com/todos'
    todos = get(todourl)
    if todos.status_code > 200:
        exit()
    todos = todos.json()
    users = get(userurl)
    if users.status_code > 200:
        exit()
    users = users.json()

    d = {u['id']: [{'task': t['title'], 'completed': t['completed'],
                    'username': u['username']}
                   for t in todos if t['userId'] == u['id']]
         for u in users}
    with open('todo_all_employees.json', 'w') as myFile:
        dump(d, myFile)
