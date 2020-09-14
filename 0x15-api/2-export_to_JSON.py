#!/usr/bin/python3
"""Script that exports data in a JSON format """
import json
import requests
from sys import argv


def export_to_json(user_id):
    """export data in the JSON format.
    Args:
        user_id (int): user id for every post
    """
    url = 'https://jsonplaceholder.typicode.com'
    users_url = "{}/users/{}".format(url, user_id)
    username = requests.get(users_url).json().get('username')
    all_tasks = requests.get('{}/todos?userId={}'.format(url, user_id)).json()

    dic = {}
    list_of_dicts = []

    for task in all_tasks:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        list_of_dicts.append(task_dict)

    with open('{}.json'.format(user_id), "w") as json_file:
        dic[user_id] = list_of_dicts
        json.dump(dic, json_file)


if __name__ == "__main__":
    export_to_json(argv[1])
