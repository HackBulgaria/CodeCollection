from hashlib import sha1


name = input('Enter name: ')
short_description = input('Enter short description: ')
tags = input('Enter tags: ').replace(' ', '').split(',')


def generate_unique_id(name, short_description, tags):
    encription = sha1()
    encription.update(name.encode('utf-8'))
    encription.update(short_description.encode('utf-8'))
    encription.update(''.join(tags).encode('utf-8'))
    unique_id = encription.hexdigest()[:16]
    return unique_id
