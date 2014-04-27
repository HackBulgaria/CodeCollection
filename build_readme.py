import os


TASKS_FOLDER = 'tasks/'


def get_unique_ids():
    unique_ids = []
    for directory in os.walk(TASKS_FOLDER):
        unique_ids.append(directory[0].split('-')[-1])
    return unique_ids


def get_task_names():
    task_names_by_id = {}
    for directory in os.walk(TASKS_FOLDER):
        for unique_id in get_unique_ids():
            if directory[0].endswith(unique_id):
                task_name = ' '.join(
                    directory[0].split('-')[:-1])[len(TASKS_FOLDER):]
                task_names_by_id[unique_id] = task_name.replace('_', ' ')
    return task_names_by_id


def get_md_for(unique_id):
    link = ''
    for subdirectory in os.walk(TASKS_FOLDER):
        for directory in subdirectory[1]:
            if directory.endswith(unique_id):
                link = '{}{}/description.md'.format(
                    TASKS_FOLDER, directory)
    return link


def build_readme():
    if not os.path.exists('readme.md'):
        with open('readme.md', 'w') as readme:
            readme.write('#CodeCollection\n')
            for unique_id, name in get_task_names().items():
                readme.write('##{}\n'.format(name))
                readme.write('[{}]({})\n'.format(
                    get_md_for(unique_id),
                    get_md_for(unique_id)))


if __name__ == '__main__':
    build_readme()
