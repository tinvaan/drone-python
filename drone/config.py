
import os


def api_token():
    if not os.environ.get('DRONE_TOKEN'):
        raise EnvironmentError('')
    return os.environ.get('DRONE_TOKEN')


def api_server():
    return os.environ.get('DRONE_SERVER', 'https://cloud.drone.io')