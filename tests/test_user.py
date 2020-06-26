
import unittest

from drone.users import Drone


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = Drone.User()

    def test_feed(self):
        builds = self.user.feed()
        self.assertGreater(len(builds), 0)
        self.assertIsInstance(builds, list)

    def test_info(self):
        user = self.user.info()
        self.assertIsInstance(user, dict)
        self.assertGreater(len(user.keys()), 0)

    def test_repos(self):
        repos = self.user.repos()
        self.assertGreater(len(repos), 0)
        self.assertIsInstance(repos, list)

    def test_sync(self):
        """TODO"""


if __name__ == '__main__':
    unittest.main()
