
from .drone import Drone
from .users import Drone as Users


class Instance:
    def __init__(self, user, repo):
        self.owner = user
        self.repository = repo

    @property
    def user(self):
        return Users.User()

    @property
    def users(self):
        return Users.Users()

    @property
    def secrets(self):
        return Users.Secrets(self.user, self.repository)

    @property
    def build(self):
        return Drone.Build(self.user, self.repository)

    @property
    def cron(self):
        return Drone.Cron(self.user, self.repository)

    @property
    def repo(self):
        return Drone.Repo(self.user, self.repository)


def drone(user, repo):
    return Instance(user, repo)
