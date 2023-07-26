#!/usr/bin/python3

"""
    module: 0-gather_data_from_an_API.py
    Interact with a REST api to get employee data
    Display employee data

    Usage:
        python3 0-gather_data_from_an_API.py <employeeId>
"""
import csv
import requests
import sys


def fetchEmployeeData(empId):
    """ fetches employee data """

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        empId)

    req = requests.get(url)

    if (req.status_code == requests.codes.ok):
        return req.json()

    return -1


def fetchEmployeeTodos(empId):
    """ fetches todos associated with the given employee id """

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        empId)

    req = requests.get(url)

    if (req.status_code == requests.codes.ok):
        return req.json()

    return -1


def presentEmployeeMetrics(empData, todoData):
    """ prints out the employee productivity data """
    name = empData.get('name')
    completed = 0
    total = len(todoData)

    for todo in todoData:
        if (todo.get('completed')):
            completed += 1

    print('Employee {} is done with tasks({}/{}):'.format(
        name, completed, total))

    for todo in todoData:
        if (todo.get('completed')):
            print('\t {}'.format(todo.get('title')))


def exportDataToCSV(empData, todoData):
    """ exports employee metric data to csv file """
    username = empData.get('username')
    userId = empData.get('id')
    csvFile = '{}.csv'.format(userId)

    with open(csvFile, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todoData:
            status = todo.get('completed')
            title = todo.get('title')

            writer.writerow([userId, username, status, title])


if __name__ == '__main__':

    args = 2

    if (len(sys.argv) == args and sys.argv[1].isdigit()):

        empId = sys.argv[1]

        empData = fetchEmployeeData(empId)
        todos = fetchEmployeeTodos(empId)

        exportDataToCSV(empData, todos)
    else:
        print('Error: Expected to receive one argument.')
        print('Usage:\n\t{} <userId>'.format(sys.argv[0]))
