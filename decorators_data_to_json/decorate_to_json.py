import functools
import json


def to_json(func):

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped


@to_json
def get_data(data):
    return  data


if __name__ == '__main__':
    print(get_data({'test': 444}))

