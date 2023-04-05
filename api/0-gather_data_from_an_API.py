#!/usr/bin/python3
''' Return information about his/her TODO list progress from an REST API '''
import requests
import sys
from sys import argv

employee_id = sys.argv[1]

url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

response = requests.get(url)

todos = response.json()

num_completed = 0
for todo in todos:
    if todo['completed']:
        num_completed += 1

print(f"Employee {todos[0]['userId']} is done with tasks ({num_completed}/{len(todos)}):")
for todo in todos:
    if todo['completed']:
        print("\t" + todo['title'])

if __name__ == '__main__':
    get_api()
