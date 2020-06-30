
import unittest
import requests

from drone.drone import Drone


class TestBuild(unittest.TestCase):
    def setUp(self):
        self.last = 1
        self.build = Drone.Build('tinvaan', 'drone-test-ci')
        for build in self.build.all():
            self.last = max(self.last, build.get('number'))

    def test_all(self):
        builds = self.build.all()
        self.assertTrue(isinstance(builds, list))
        for build in builds:
            self.assertEqual('tinvaan', build.get('sender'))
            self.assertEqual('tinvaan', build.get('author_login'))

    def test_info(self):
        first = self.build.info(1)
        self.assertEqual(first.get('number'), 1)
        self.assertEqual(first.get('status'), 'success')

        with self.assertRaises(requests.HTTPError) as err:
            self.build.info(100)
            self.assertEqual(err.response.status_code, 404)

            self.build.info('foobar')
            self.assertEqual(err.response.status_code, 404)

    def test_logs(self):
        """TODO: API needs better documentation"""
        for log in self.build.logs(1, 1, 1):
            self.assertListEqual(list(log.keys()), ['pos', 'out', 'time'])
        with self.assertRaises(requests.HTTPError) as err:
            self.build.logs(1, 'foo', 'bar')
            self.assertEqual(err.response.status_code, 404)

    def test_promote(self):
        """TODO: """

    def test_approve(self):
        """TODO: Create a pending build to be approved"""
        with self.assertRaises(requests.HTTPError) as err:
            self.build.approve(1)

    def test_decline(self):
        """TODO: Create a pending build to be declined"""
        with self.assertRaises(requests.HTTPError) as err:
            self.build.decline(1)

    def test_restart(self):
        response = self.build.restart(self.last)
        self.assertEqual(response.get('status'), 'pending')
        self.assertEqual(response.get('number'), self.last + 1)
        self.assertEqual(response.get('author_login'), 'tinvaan')

    def test_stop(self):
        response = self.build.stop(self.last)
        self.assertEqual(response.get('number'), self.last)
        self.assertEqual(response.get('status'), 'killed')


if __name__ == '__main__':
    unittest.main()
