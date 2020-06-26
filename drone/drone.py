
import requests

from . import http, config


class Action:
    def __init__(self, **kwargs):
        self.host = config.api_server()
        self.token = config.api_token()
        self.user = kwargs.get('user')
        self.repo = kwargs.get('repo')
        self.cron = kwargs.get('cron')

    def all(self):
        return http.get(self.route)

    def logs(self, name, stage, step):
        raise NotImplementedError()

    def create(self, namespace, build, **kwargs):
        raise NotImplementedError()

    def info(self, name):
        return http.get('%s/%s' % (self.route, name))

    def stop(self, name):
        return http.delete('%s/%s' % (self.route, name))

    def restart(self, name):
        return http.post('%s/%s' % (self.route, name))

    def approve(self, name):
        return http.post('%s/%s/approve' % (self.route, name))

    def decline(self, name):
        return http.post('%s/%s/decline' % (self.route, name))

    def promote(self, name, **kwargs):
        return http.post('%s/%s/promote' % (self.route, name))


class Drone:
    class Build(Action):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            assert self.user is not None
            assert self.repo is not None
            self.route = '%s/api/repos/%s/%s/builds' % (
                self.host, self.user, self.repo)

        def create(self, ns, build, **kwargs):
            url = self.host + '/api/repos/%s/%s/builds' % (ns, build)
            return http.post(url, params=kwargs)

        def logs(self, build, stage, step):
            return http.get('%s/%s/logs/%s/%s' % (self.route, build, stage, step))


    class Cron(Action):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            assert self.user is not None
            assert self.repo is not None
            assert self.cron is not None
            self.route = '%s/api/repos/%s/%s/cron' % (
                self.host, self.user, self.repo)

        def delete(self):
            return http.delete('%s/%s' % (self.route, self.cron))

        def create(self, **kwargs):
            return http.post(self.route, data=kwargs)

        def update(self, **kwargs):
            return http.patch('%s/%s' % (self.route, self.cron), data=kwargs)


    class Repo(Action):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            assert self.user is not None
            assert self.repo is not None
            self.route = '%s/api/repos/%s/%s' % (self.host, self.user, self.repo)

        def info(self):
            return http.get(self.route)

        def enable(self):
            return http.post(self.route)

        def disable(self):
            return http.delete(self.route)

        def repair(self):
            return http.post(self.route + '/repair')

        def update(self, **kwargs):
            return http.patch(self.route, data=kwargs)
