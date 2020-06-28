
import json
import requests

from . import config
from .decorators import jsonargs


@jsonargs
def get(url, params=None):
    headers = {'Authorization': 'Bearer %s' % config.api_token()}
    r = requests.get(url, headers=headers) if not params else \
        requests.get(url, headers=headers, params=params)
    if not r.ok:
        r.raise_for_status()
    return r.json()


@jsonargs
def post(url, params=None, data=None):
    headers = {'Authorization': 'Bearer %s' % config.api_token()}
    if params and data:
        r = requests.post(url, headers=headers, params=params, data=data)
    elif params:
        r = requests.post(url, headers=headers, params=params)
    elif data:
        r = requests.post(url, headers=headers, data=data)
    else:
        r = requests.post(url, headers=headers)
    if not r.ok:
        r.raise_for_status()
    return r.json()


@jsonargs
def patch(url, params=None, data=None):
    headers = {'Authorization': 'Bearer %s' % config.api_token()}
    if params and data:
        r = requests.patch(url, headers=headers, params=params, data=data)
    elif params:
        r = requests.patch(url, headers=headers, params=params)
    elif data:
        r = requests.patch(url, headers=headers, data=data)
    else:
        r = requests.patch(url, headers=headers)
    if not r.ok:
        r.raise_for_status()
    return r.json()


def delete(url):
    headers = {'Authorization': 'Bearer %s' % config.api_token()}
    r = requests.delete(url, headers=headers)
    if not r.ok:
        r.raise_for_status()
    return r.json()
