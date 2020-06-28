
import json


def jsonargs(func):
    def wrapper(*args, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                kwargs.update({key: json.dumps(value)})
        return func(*args, **kwargs)
    return wrapper
