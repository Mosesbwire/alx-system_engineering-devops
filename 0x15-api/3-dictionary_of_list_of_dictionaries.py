#!/usr/bin/python3

"""
    module: 3-dictionary_of_list_of_dictionaries.py
    Interact with a REST api to get employee data
    Display employee data

    Usage:
        python3 0-gather_data_from_an_API.py <employeeId>
"""
import json
import requests
import sys


def fetchEmployees():
    """ fetches all employees data """

    url = 'https://jsonplaceholder.typicode.com/users'

    req = requests.get(url)

    if (req.status_code == requests.codes.ok):
        return req.json()

    return -1


def fetchTodos():
    """ fetches all todos """

    url = 'https://jsonplaceholder.typicode.com/todos'

    req = requests.get(url)

    if (req.status_code == requests.codes.ok):
        return req.json()

    return -1


def exportDataInJSON(employees, todos):
    """ exports employee metric data to json file """
    fileName = 'todo_all_employees.json'
    fileContent = {}
    for employee in employees:
        username = employee.get('username')
        userId = employee.get('id')
        dataObj = {"username": username}
        dataList = []
        for todo in todos:
            dataObj["task"] = todo.get('task')
            dataObj["completed"] = todo.get('completed')
            dataList.append(dataObj)

        fileContent[userId] = dataList

    with open(fileName, 'w') as file:
        json.dump(fileContent, file)


if __name__ == '__main__':

    employees = fetchEmployees()
    todos = fetchTodos()

    exportDataInJSON(employees, todos)
