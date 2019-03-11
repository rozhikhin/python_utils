import argparse
import json
import tempfile
from os import path, remove

storage_path = path.join(tempfile.gettempdir(), 'storage.data')


def init(file_path):
    if not path.exists(file_path):
        with open(file_path, "a") as file:
            json.dump([], file)


def clear():
    remove(storage_path)


def set_value(data_to_save):
    with open(storage_path, "r+") as file:
        data_from_file = json.load(file)

    with open(storage_path, "w") as file:
        data_from_file.append(data_to_save)
        json.dump(data_from_file, file)


def get_value(key_to_get):
    with open(storage_path, "r+") as file:
        data_from_file = json.load(file)
        result = ''
        for item in data_from_file:
            value = item.get(key_to_get, None)
            if value:
                result += ", " + value

        print(result.lstrip(", "))


if __name__ == '__main__':

    init(storage_path)

    parser = argparse.ArgumentParser()
    parser.add_argument("--key",  help='Key')
    parser.add_argument("--val", help='Value')
    parser.add_argument("--clear", action='store_true', help='Clear')

    args = parser.parse_args()

    if args.clear:
        clear()
    elif args.key and args.val:
        data = {args.key: args.val}
        set_value(data)
    elif args.key:
        key = args.key
        get_value(key)
    else:
        print('Некорректный ввод данных')





