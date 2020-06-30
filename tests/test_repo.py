
import unittest
import requests

from drone.drone import Drone


class TestRepo(unittest.TestCase):
    def setUp(self):
        self.repo = Drone.Repo('tinvaan', 'drone-test-ci')

    def test_chown(self):
        """ TODO: API needs better documentation.
            How should an example payload look like?
        """

    def test_all(self):
        self.assertGreater(len(self.repo.all()), 1)
        self.assertGreater(len(Drone.Repo('tinvaan', 'foobar').all()), 1)
        self.assertGreater(len(Drone.Repo('foobar', 'drone-ci-test').all()), 1)

    def test_enable(self):
        self.assertEqual(list(self.repo.enable().keys()), [
            'id', 'uid', 'user_id', 'namespace', 'name', 'slug', 'scm',
            'git_http_url', 'git_ssh_url', 'link', 'default_branch', 'private',
            'visibility', 'active', 'config_path', 'trusted', 'protected',
            'ignore_forks', 'ignore_pull_requests', 'auto_cancel_pull_requests',
            'auto_cancel_pushes', 'timeout', 'counter', 'synced', 'created',
            'updated', 'version'])
        with self.assertRaises(requests.HTTPError) as err:
            Drone.Repo('tinvaan', 'foobar').enable()
            self.assertEqual(err.response.status_code, 404)

            Drone.Repo('foobar', 'barfoo').enable()
            self.assertEqual(err.response.status_code, 404)

    def test_disable(self):
        self.assertEqual(list(self.repo.enable().keys()), [
            'id', 'uid', 'user_id', 'namespace', 'name', 'slug', 'scm',
            'git_http_url', 'git_ssh_url', 'link', 'default_branch', 'private',
            'visibility', 'active', 'config_path', 'trusted', 'protected',
            'ignore_forks', 'ignore_pull_requests', 'auto_cancel_pull_requests',
            'auto_cancel_pushes', 'timeout', 'counter', 'synced', 'created',
            'updated', 'version'])
        with self.assertRaises(requests.HTTPError) as err:
            Drone.Repo('tinvaan', 'foobar').disable()
            self.assertEqual(err.response.status_code, 404)

            Drone.Repo('foobar', 'barfoo').disable()
            self.assertEqual(err.response.status_code, 404)

    def test_info(self):
        self.assertEqual(list(self.repo.info()), [
            'id', 'uid', 'user_id', 'namespace', 'name', 'slug', 'scm',
            'git_http_url', 'git_ssh_url', 'link', 'default_branch', 'private',
            'visibility', 'active', 'config_path', 'trusted', 'protected',
            'ignore_forks', 'ignore_pull_requests', 'auto_cancel_pull_requests',
            'auto_cancel_pushes', 'timeout', 'counter', 'synced', 'created',
            'updated', 'version', 'permissions'])
        with self.assertRaises(requests.HTTPError) as err:
            Drone.Repo('tinvaan', 'foobar').info()
            self.assertEqual(err.response.status_code, 404)

            Drone.Repo('foobar', 'barfoo').info()
            self.assertEqual(err.response.status_code, 404)

    def test_repair(self):
        repair = self.repo.repair()
        self.assertEqual(list(repair.keys()), [
            'id', 'uid', 'user_id', 'namespace', 'name', 'slug', 'scm',
            'git_http_url', 'git_ssh_url', 'link', 'default_branch', 'private',
            'visibility', 'active', 'config_path', 'trusted', 'protected',
            'ignore_forks', 'ignore_pull_requests', 'auto_cancel_pull_requests',
            'auto_cancel_pushes', 'timeout', 'counter', 'synced', 'created',
            'updated', 'version'])
        with self.assertRaises(requests.HTTPError) as err:
            Drone.Repo('tinvaan', 'foobar').repair()
            self.assertEqual(err.response.status_code, 404)

            Drone.Repo('foobar', 'drone-ci-test')
            self.assertEqual(err.response.status_code, 404)

            Drone.Repo('foobar', 'barfoo').repair()
            self.assertEqual(err.response.status_code, 404)

    def test_update(self):
        params = {
            'config_path': '.drone.test.yml',
            'visibility': 'internal',
            'protected': False,
            'trusted': False,
            'timeout': 60,
        }
        response = self.repo.update(**params)
        self.assertEqual(response.get('config_path'), '.drone.test.yml')
        self.assertEqual(list(response.keys()), [
            'id', 'uid', 'user_id', 'namespace', 'name', 'slug', 'scm',
            'git_http_url', 'git_ssh_url', 'link', 'default_branch', 'private',
            'visibility', 'active', 'config_path', 'trusted', 'protected',
            'ignore_forks', 'ignore_pull_requests', 'auto_cancel_pull_requests',
            'auto_cancel_pushes', 'timeout', 'counter', 'synced', 'created',
            'updated', 'version'])

        params = {'config_path': '.drone.yml'}
        response = self.repo.update(**params)
        self.assertEqual(response.get('config_path'), '.drone.yml')
        self.assertEqual(list(response.keys()), [
            'id', 'uid', 'user_id', 'namespace', 'name', 'slug', 'scm',
            'git_http_url', 'git_ssh_url', 'link', 'default_branch', 'private',
            'visibility', 'active', 'config_path', 'trusted', 'protected',
            'ignore_forks', 'ignore_pull_requests', 'auto_cancel_pull_requests',
            'auto_cancel_pushes', 'timeout', 'counter', 'synced', 'created',
            'updated', 'version'])


if __name__ == '__main__':
    unittest.main()
