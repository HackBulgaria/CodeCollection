import json
import os
from new_task import import_index_json as import_json
from new_task import get_latest_index


TASKS_FOLDER = "tasks/"


def get_unique_ids():
    unique_ids = []
    for directory in os.walk(TASKS_FOLDER):
        unique_ids.append(directory[0].split('-')[-1])
    return unique_ids


def get_data_for(unique_id):
    for subdirectory in os.walk(TASKS_FOLDER):
        for directory in subdirectory[1]:
            if directory.endswith(unique_id):
                filename = '{}{}/metadata.json'.format(TASKS_FOLDER, directory)
                data = import_json(filename)
    return data


def build_index():
    if not os.path.exists('index.json'):
        with open('index.json', 'w') as index_json:
            data = {}
            for unique_id in get_unique_ids()[1:]:
                all_data = get_data_for(unique_id)
                data[unique_id] = {'name': all_data['name'],
                                   'tags': all_data['tags'],
                                   'index': get_latest_index(data) + 1}
            index_json.write((json.dumps(data, indent=4)))

if __name__ == '__main__':
    build_index()
