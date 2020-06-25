
import requests

from .config import host, token


class Action:
    def __init__(self, **kwargs):
        assert host is not None
        assert token is not None
        self.user = kwargs.get('user')
        self.repo = kwargs.get('repo')
        self.cron = kwargs.get('cron')

    def logs(self, name, stage, step):
        raise NotImplementedError()

    def create(self, namespace, build, **kwargs):
        raise NotImplementedError()

    def history(self):
        return requests.get(self.route).json()

    def info(self, name):
        return requests.get('%s/%s' % (self.route, name)).json()

    def stop(self, name):
        return requests.delete('%s/%s' % (self.route, name)).json()

    def restart(self, name):
        return requests.post('%s/%s' % (self.route, name)).json()

    def approve(self, name):
        return requests.post('%s/%s/approve' % (self.route, name)).json()

    def decline(self, name):
        return requests.post('%s/%s/decline' % (self.route, name)).json()

    def promote(self, name, **kwargs):
        return requests.post('%s/%s/promote' % (self.route, name)).json()


class Drone:
    class Build(Action):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            assert self.user is not None
            assert self.repo is not None
            self.route = host + '/api/repos/%s/%s/builds' % (self.user, self.repo)

        def create(self, ns, build, **kwargs):
            url = host + '/api/repos/%s/%s/builds' % (ns, build)
            return requests.post(url, params=kwargs).json()

        def logs(self, build, stage, step):
            return requests.get(
                self.route + '/%s/logs/%s/%s' % (build, stage, step)).json()


    class Cron(Action):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            assert self.user is not None
            assert self.repo is not None
            assert self.cron is not None
            self.route = host + '/api/repos/%s/%s/cron' % (self.user, self.repo)

        def delete(self):
            return requests.delete(self.route + '/%s' % self.cron).json()

        def create(self, **kwargs):
            return requests.post(self.route, data=kwargs).json()

        def update(self, **kwargs):
            return requests.patch(self.route + '/%s' % self.cron, data=kwargs).json()


    class Repo(Action):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            assert self.user is not None
            assert self.repo is not None
            self.route = host + '/api/repos/%s/%s' % (self.user, self.repo)

        def info(self):
            return requests.get(self.route).json()

        def enable(self):
            return requests.post(self.route).json()

        def disable(self):
            return requests.delete(self.route).json()

        def repair(self):
            return requests.post(self.route + '/repair').json()

        def update(self, **kwargs):
            return requests.patch(self.route, data=kwargs).json()
