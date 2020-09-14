#!/usr/bin/python3
"""
Script that exports data in a JSON format
(For all tasks from all employees)
"""
import json
import requests


def todo_all_emp():
    """cript to export data in the JSON format.
    Args:
        user_id (int): user id of the
        of to do list
    """
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get("{}/users".format(url)).json()

    dic = {}
    user_dict = {}

    for user in users:
        user_id = user.get('id')
        dic[user_id] = []
        user_dict[user_id] = user.get('username')

    todos = requests.get("{}/todos".format(url)).json()

    for task in todos:
        task_dict_emp = {}
        user_id = task.get('userId')
        task_dict_emp["task"] = task.get('title')
        task_dict_emp["completed"] = task.get('completed')
        task_dict_emp["username"] = user_dict.get(user_id)
        dic.get(user_id).append(task_dict_emp)

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(dic, json_file)


if __name__ == "__main__":
    todo_all_emp()
