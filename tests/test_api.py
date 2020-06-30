
import unittest

from unittest.mock import MagicMock

from drone.api import drone
from drone.drone import Drone
from drone.users import Drone as Users


class TestApi(unittest.TestCase):
    def setUp(self):
        self.drone = drone('tinvaan', 'drone-test-ci')

    def test_user(self):
        mock = Users.User
        mock.__init__ = MagicMock(return_value=None)
        self.drone.user
        mock.__init__.assert_called()

        mock.feed = MagicMock(return_value=dict)
        self.drone.user.feed()
        mock.feed.assert_called()

        mock.info = MagicMock(return_value=dict)
        self.drone.user.info()
        mock.info.assert_called()

        mock.repos = MagicMock(return_value=dict)
        args = {'foo': 'bar', 'bar': 'foo'}
        self.drone.user.repos(**args)
        mock.repos.assert_called()

        mock.sync = MagicMock(return_value=dict)
        self.drone.user.sync(**args)
        mock.sync.assert_called()

    def test_users(self):
        mock = Users.Users
        mock.__init__ = MagicMock(return_value=None)
        self.drone.users
        mock.__init__.assert_called()

        mock.all = MagicMock(return_value=list)
        self.drone.users.all()
        mock.all.assert_called()

        mock.info = MagicMock(return_value=dict)
        self.drone.users.info()
        mock.info.assert_called()

        mock.delete = MagicMock(return_value=dict)
        self.drone.users.delete()
        mock.delete.assert_called()

        mock.create = MagicMock(return_value=dict)
        args = {'foo': 'bar', 'bar': 'foo'}
        self.drone.users.create(**args)
        mock.create.assert_called()

        mock.update = MagicMock(return_value=dict)
        self.drone.users.update(**args)
        mock.update.assert_called()

    def test_secrets(self):
        mock = Users.Secrets
        mock.__init__ = MagicMock(return_value=None)
        self.drone.secrets
        mock.__init__.assert_called()

        mock.all = MagicMock(return_value=list)
        self.drone.secrets.all()
        mock.all.assert_called()

        mock.info = MagicMock(return_value=dict)
        self.drone.secrets.info('foobar')
        mock.info.assert_called()

        mock.update = MagicMock(return_value=dict)
        args = {'foo': 'bar', 'bar': 'foo'}
        self.drone.secrets.update('foobar', **args)
        mock.update.assert_called()

        mock.delete = MagicMock(return_value=dict)
        self.drone.secrets.delete('foobar')
        mock.delete.assert_called()

    def test_build(self):
        mock = Drone.Build
        mock.__init__ = MagicMock(return_value=None)
        self.drone.build
        mock.__init__.assert_called()

        mock.all = MagicMock(return_value=list)
        self.drone.build.all()
        mock.all.assert_called()

        mock.approve = MagicMock(return_value=dict)
        self.drone.build.approve(1)
        mock.approve.assert_called()

        mock.decline = MagicMock(return_value=dict)
        self.drone.build.decline(1)
        mock.decline.assert_called()

        mock.promote = MagicMock(return_value=dict)
        self.drone.build.promote(1)
        mock.promote.assert_called()

        mock.restart = MagicMock(return_value=dict)
        self.drone.build.restart(1)
        mock.restart.assert_called()

        mock.stop = MagicMock(return_value=dict)
        self.drone.build.stop(1)
        mock.stop.assert_called()

    def test_cron(self):
        mock = Drone.Cron
        mock.__init__ = MagicMock(return_value=None)
        self.drone.cron
        mock.__init__.assert_called()

        mock.all = MagicMock(return_value=dict)
        self.drone.cron.all()
        mock.all.assert_called()

        mock.info = MagicMock(return_value=dict)
        self.drone.cron.info(1)
        mock.info.assert_called()

        mock.delete = MagicMock(return_value=dict)
        self.drone.cron.delete(1)
        mock.delete.assert_called()

        mock.create = MagicMock(return_value=dict)
        args = {'foo': 'bar', 'bar': 'foo'}
        self.drone.cron.create(**args)
        mock.create.assert_called()

        mock.update = MagicMock(return_value=dict)
        self.drone.cron.update(1, **args)
        mock.update.assert_called()

    def test_repo(self):
        mock = Drone.Repo
        mock.__init__ = MagicMock(return_value=None)
        self.drone.repo
        mock.__init__.assert_called()

        mock.all = MagicMock(return_value=list)
        self.drone.repo.all()
        mock.all.assert_called()

        mock.info = MagicMock(return_value=dict)
        self.drone.repo.info()
        mock.info.assert_called()

        mock.chown = MagicMock(return_value=dict)
        args = {'foo': 'bar', 'bar': 'foo'}
        self.drone.repo.chown(**args)
        mock.chown.assert_called()

        mock.disable = MagicMock(return_value=dict)
        self.drone.repo.disable()
        mock.disable.assert_called()

        mock.enable = MagicMock(return_value=dict)
        self.drone.repo.enable()
        mock.enable.assert_called()

        mock.repair = MagicMock(return_value=dict)
        self.drone.repo.repair()
        mock.repair.assert_called()

        mock.update = MagicMock(return_value=dict)
        self.drone.repo.update(**args)
        mock.update.assert_called()


if __name__ == '__main__':
    unittest.main()
