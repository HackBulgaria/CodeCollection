from hashlib import sha1
import json
import os
from time import time


TASKS_FOLDER = "tasks/"


def ensure_or_create(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def import_index_json(filename):
    with open(filename) as data_file:
        try:
            data = json.load(data_file)
        except ValueError:
            data = {}
    return data


def generate_unique_id(name, short_description, tags):
    encription = sha1()
    encription.update(name.encode('utf-8'))
    encription.update(short_description.encode('utf-8'))
    encription.update(''.join(tags).encode('utf-8'))
    encription.update(str(time()).encode('utf-8'))
    unique_id = encription.hexdigest()[:16]
    return unique_id


def get_latest_index(data):
    latest = 0

    for key in data:
        if data[key]["index"] > latest:
            latest = data[key]["index"]

    return latest


def generate_metadata(unique_id, name, tags, short_description):
    result = {
        "unique_id": unique_id,
        "name": name,
        "short_description": short_description,
        "tags": tags
    }

    return result


def generate_task_name(name, unique_id):
    name = name.replace(" ", "_").lower()
    return "{}-{}".format(name, unique_id)


def generate_description_md(name, short_description):
    template = "# {} \n\n {} \n"
    return template.format(name, short_description)


def write_metadata(path, metadata):
    file_name = path + "/metadata.json"
    handle = open(file_name, "w")
    handle.write(json.dumps(metadata, indent=4))
    handle.close()


def write_description(path, description_md):
    file_name = path + "/description.md"
    handle = open(file_name, "w")
    handle.write(description_md)
    handle.close()


def update_index(index_data, metadata):
    unique_id = metadata["unique_id"]
    index_data[unique_id] = {
        "tags": metadata["tags"],
        "index": get_latest_index(index_data) + 1,
        "name": metadata["name"]
    }


def write_index(index_data):
    handle = open("index.json", "w")
    handle.write(json.dumps(index_data, indent=4))
    handle.close()


def main():
    ensure_or_create(TASKS_FOLDER)
    index_data = import_index_json('index.json')
    print(index_data)
    name = input('Enter name: ')
    short_description = input('Enter short description: ')
    tags = input('Enter tags: ').replace(' ', '').split(',')

    unique_id = generate_unique_id(name, short_description, tags)
    print(unique_id)

    while unique_id in index_data:
        print("WARNING:{} found in index".format(unique_id))
        unique_id = generate_unique_id(name, short_description, tags)

    metadata = generate_metadata(unique_id, name, tags, short_description)
    description_md = generate_description_md(name, short_description)

    create_path = TASKS_FOLDER + generate_task_name(name, unique_id)
    ensure_or_create(create_path)

    write_metadata(create_path, metadata)
    write_description(create_path, description_md)
    update_index(index_data, metadata)
    write_index(index_data)

if __name__ == '__main__':
    main()
