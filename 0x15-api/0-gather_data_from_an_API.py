#!/usr/bin/python3
"""TODO list progress"""
from requests import get
from sys import argv


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
user = user.json()['name']
done_tasks = [task['title'] for task in todos if task['completed']]
msg = 'Employee {} is done with tasks({}/{}):'.format(user, len(done_tasks),
                                                      len(todos))
done_tasks = '{}\n\t {}'.format(msg, '\n\t '.join(done_tasks))
if __name__ == "__main__":
    print(done_tasks)
