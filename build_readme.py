import os
import json


TASKS_FOLDER = 'tasks/'


def get_unique_ids():
    unique_ids = []
    for directory in os.walk(TASKS_FOLDER):
        unique_ids.append(directory[0].split('-')[-1])
    return unique_ids


def import_index_json(filename):
    with open(filename) as data_file:
        try:
            data = json.load(data_file)
        except ValueError:
            data = {}
    data_file.close()
    return data


def get_data_by_id():
    data_by_id = {}
    for directory in os.walk(TASKS_FOLDER):
        for unique_id in get_unique_ids():
            if directory[0].endswith(unique_id)\
                    and directory[0] != TASKS_FOLDER:
                short_description = import_index_json(
                    directory[0] + '/metadata.json')['short_description']
                task_name = ' '.join(
                    directory[0].split('-')[:-1])[len(TASKS_FOLDER):]
                data_by_id[unique_id] = [task_name.replace('_', ' '),
                                         short_description]
                break
    return data_by_id


def get_md_for(unique_id):
    link = ''
    for subdirectory in os.walk(TASKS_FOLDER):
        for directory in subdirectory[1]:
            if directory.endswith(unique_id):
                link = '{}{}/description.md'.format(
                    TASKS_FOLDER, directory)
    return link


def build_readme():
    with open('README.md', 'w') as readme:
        readme.write('# CodeCollection\n')
        data = get_data_by_id()
        for unique_id, info in data.items():
            readme.write('## [{}]({})\n'.format(
                info[0], get_md_for(unique_id)))
            readme.write('{}\n\n'.format(info[1]))


if __name__ == '__main__':
    build_readme()
