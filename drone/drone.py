
import requests

from . import http, config


class Actions:
    def __init__(self, user, repo):
        self.user = user
        self.repo = repo
        self.host = config.api_server()
        self.token = config.api_token()

    def __check__(self):
        """ TODO: There should be a way to check if secret
            provided matches against the username in the request
        """
        try:
            secret = http.get('%s/api/repos/%s/%s/secrets/%s' % (
                self.host, self.user, self.repo, self.token))
            if secret.get('name') != self.user:
                raise EnvironmentError('Secrets for %s do not match' % self.user)
        except requests.HTTPError as err:
            if err.response.status_code in range(400, 500):
                raise EnvironmentError('Secrets for %s do not match' % self.user)
            raise err

    def all(self):
        return http.get(self.route)

    def info(self, name):
        return http.get('%s/%s' % (self.route, name))

    def view(self, name):
        return self.info(name)

    def delete(self, name):
        raise NotImplementedError()

    def create(self, **kwargs):
        raise NotImplementedError()

    def update(self, name, **kwargs):
        raise NotImplementedError()



class Drone:
    class Build(Actions):
        def __init__(self, user, repo):
            super().__init__(user, repo)
            self.route = '%s/api/repos/%s/%s/builds' % (
                self.host, self.user, self.repo)

        def create(self, ns, build, **kwargs):
            url = self.host + '/api/repos/%s/%s/builds' % (ns, build)
            return http.post(url, params=kwargs)

        def logs(self, build, stage, step):
            return http.get(
                '%s/%s/logs/%s/%s' % (self.route, build, stage, step))

        def promote(self, build, , target, **kwargs):
            return http.post('%s/%s/promote?target=%s' % (self.route, build, target))

        def decline(self, build):
            return http.post('%s/%s/decline' % (self.route, build))

        def approve(self, build):
            return http.post('%s/%s/approve' % (self.route, build))

        def restart(self, build):
            return http.post('%s/%s' % (self.route, build))

        def stop(self, build):
            return http.delete('%s/%s' % (self.route, build))


    class Cron(Actions):
        def __init__(self, user, repo):
            super().__init__(user, repo)
            self.route = '%s/api/repos/%s/%s/cron' % (
                self.host, self.user, self.repo)

        def delete(self, cron):
            return http.delete('%s/%s' % (self.route, cron))

        def create(self, **kwargs):
            return http.post(self.route, data=kwargs)

        def update(self, cron, **kwargs):
            return http.patch('%s/%s' % (self.route, cron), data=kwargs)


    class Repo(Actions):
        def __init__(self, user, repo):
            super().__init__(user, repo)
            self.route = '%s/api/repos/%s/%s' % (self.host, self.user, self.repo)

        def all(self):
            return http.get('%s/api/user/repos' % self.host)

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

        def chown(self, **kwargs):
            return http.post(self.route + '/chown', data=kwargs)
    
