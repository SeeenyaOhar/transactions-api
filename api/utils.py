from flask import request
from ..exceptions import NoBodyProvided
from datetime import datetime


def inject_body(func):
    def wrapper(*args, **kwargs):
        json_data = request.json
        if json_data is None:
            raise NoBodyProvided()
        return func(json_data)

    wrapper.__name__ = func.__name__
    return wrapper

def remove_key_id(key: str, obj: dict):
    if key in obj:
        obj.pop(key)


def remove_id(obj: dict):
    if 'id' in obj:
        obj.pop('id')

def convert_datetime(key: str, obj: dict, format='%m/%d/%y %H:%M:%S'):
    if key in obj:
        obj[key] = datetime.strptime(obj[key], format)