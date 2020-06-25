
import requests

from .config import host


class Drone:
    class Secrets:
        def __init__(self, user, repo):
            self.user = user
            self.repo = repo
            self.route = host + '/api/repos/%s/%s/secrets' % (self.user, self.repo)

        def info(self, secret):
            return requests.get('%s/%s' % (self.route, secret)).json()

        def history(self):
            return requests.get(self.route).json()

        def create(self, **kwargs):
            return requests.post(self.route, data=kwargs).json()

        def update(self, secret):
            return requests.post('%s/%s' % (self.route, secret)).json()

        def delete(self, secret):
            return requests.delete('%s/%s' % (self.route, secret)).json()


    class User:
        def __init__(self):
            self.route = host + '/api/users'

        def history(self):
            return requests.get(self.route).json()

        def create(self, **kwargs):
            return requests.post(self.route, data=kwargs).json()

        def update(self, login):
            return requests.patch('%s/%s' % (self.route, login)).json()

        def delete(self, login):
            return requests.delete('%s/%s' % (self.route, login)).json()

        def builds(self):
            return requests.get(self.route + '/builds').json()

        def repos(self, sync=False, **kwargs):
            if not sync:
                return requests.get(self.route + '/repos').json()
            return requests.post(self.route + '/repos', data=kwargs).json()

        def info(self, user=None):
            if not user:
                return requests.get(self.route).json()
            return requests.get('%s/%s' % (self.route, user)).json()
