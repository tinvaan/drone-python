
import os


token = os.environ.get('DRONE_TOKEN')
host = os.environ.get('DRONE_SERVER')
host = host if host is not None else 'https://cloud.drone.io'
