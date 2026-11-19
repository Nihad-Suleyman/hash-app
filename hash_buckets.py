import sys
import os
import json
import hashlib


def get_bucket(text, n):
    hash_value = hashlib.blake2b(text.encode('utf-8'), digest_size=8).hexdigest()
    number = int(hash_value, 16)
    return number % n + 1


def save_links(links):
    with open('links.json', 'w') as file:
        json.dump(links, file, indent=4)


def add_text(text, bucket, size, links):
    filename = str(bucket) + '.txt'

    while links[filename] is not None:
        filename = links[filename]

    while len(text) > 0:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        free_space = size - len(content)

        if free_space == 0:
            count = 1
            new_file = str(bucket) + '_overflow_' + str(count) + '.txt'
            while os.path.exists(new_file):
                count += 1
                new_file = str(bucket) + '_overflow_' + str(count) + '.txt'

            with open(new_file, 'w', encoding='utf-8'):
                pass

            links[filename] = new_file
            links[new_file] = None
            save_links(links)
            filename = new_file
            free_space = size

        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text[:free_space])

        print('Written to:', filename)
        text = text[free_space:]
