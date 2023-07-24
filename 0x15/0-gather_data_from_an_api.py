#!/usr/bin/python3

"""
    uses the request http library to make api calls
"""

import requests
import sys


payload = {'userId': sys.argv[1]}
req = requests.get(
    'https://jsonplaceholder.typicode.com/todos', params=payload)
req2 = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))

if (req.status_code == requests.codes.ok):
    user = req2.json()
    todos = req.json()
    name = user.get('name')
    complete = 0
    for todo in todos:
        if (todo.get('completed')):
            complete += 1
    total = len(todos)
    print('Employee {} is done with tasks({}/{}):'.format(
        name, complete, total))

    for todo in todos:
        if(todo.get('completed')):
            print('\t {}'.format(todo.get('title')))

else:
    print('failed to fetch resources')
