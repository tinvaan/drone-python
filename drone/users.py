
from . import http, config


class Drone:
    class Secrets:
        def __init__(self, user, repo):
            self.user = user
            self.repo = repo
            self.route = '%s/api/repos/%s/%s/secrets' % (
                config.api_server(), self.user, self.repo)

        def all(self):
            return http.get(self.route)

        def info(self, secret):
            return http.get('%s/%s' % (self.route, secret))

        def create(self, **kwargs):
            return http.post(self.route, data=kwargs)

        def update(self, secret):
            return http.post('%s/%s' % (self.route, secret))

        def delete(self, secret):
            return http.delete('%s/%s' % (self.route, secret))


    class User:
        def __init__(self):
            self.route = '%s/api/user' % config.api_server()

        def feed(self):
            return http.get(self.route + '/builds')

        def info(self):
            return http.get(self.route)

        def repos(self, **kwargs):
            return http.get(self.route + '/repos', params=kwargs)

        def sync(self, **kwargs):
            return http.post(self.route + '/repos', data=kwargs)


    class Users:
        def __init__(self):
            self.route = '%s/api/users' % config.api_server()

        def all(self):
            return http.get(self.route)

        def info(self, user):
            return http.get('%s/%s' % (self.route, user))

        def delete(self, user):
            return http.get('%s/%s' % (self.route, user))

        def create(self, **kwargs):
            return http.post(self.route, data=kwargs)

        def update(self, user, **kwargs):
            return http.post('%s/%s' % (self.route, user), data=kwargs)
