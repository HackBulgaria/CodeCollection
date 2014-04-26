from hashlib import sha1
import json
import os


def import_index_json(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data


def generate_unique_id(name, short_description, tags):
    encription = sha1()
    encription.update(name.encode('utf-8'))
    encription.update(short_description.encode('utf-8'))
    encription.update(''.join(tags).encode('utf-8'))
    unique_id = encription.hexdigest()[:16]
    return unique_id


def main():
    index_data = import_index_json('index.json')
    print(index_data)
    name = input('Enter name: ')
    short_description = input('Enter short description: ')
    tags = input('Enter tags: ').replace(' ', '').split(',')
    print(generate_unique_id(name, short_description, tags))
    unique_id = generate_unique_id(name, short_description, tags)
    md_path = unique_id + '/description.md'
    json_path = unique_id + '/metadata.json'
    if unique_id not in index_data:
        index_data[unique_id] = {('[' + ', '.join(tags) + ']')}
        if not os.path.exists(unique_id):
            index = 1
            os.makedirs(unique_id)
            with open(json_path, 'w') as metadata:
                metadata.write(
                    json.dumps(
                        {'tags': tags,
                         'name': name,
                         'unique_id': unique_id,
                         'short_description': short_description},
                        metadata, indent=4))
                metadata.close()
            with open(md_path, 'w') as description:
                description.write('#{}\n\n{}'.format(name, short_description))
                description.close()
            if os.path.exists(json_path) and os.path.exists(md_path):
                with open('index.json', 'w') as file:
                    if index_data != {}:
                        index = index_data[unique_id]['index'] + 1
                    file.write(
                        json.dumps(
                            {unique_id: {
                                'index': index,
                                'tags': tags
                            }},
                            file, indent=4))
                    file.close()
    print(index_data)


if __name__ == '__main__':
    main()
