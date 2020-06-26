
import unittest
import requests

from drone.users import Drone


class TestSecrets(unittest.TestCase):
    def setUp(self):
        kwargs = {
            'name': 'Testsecret', 'data': 'This is a test', 'pull_request': False
        }
        self.secret = Drone.Secrets('tinvaan', 'drone-test-ci').create(**kwargs)

    def test_all(self):
        self.assertEqual(
            Drone.Secrets('tinvaan', 'orara').all(), [])
        self.assertGreater(
            len(Drone.Secrets('tinvaan', 'drone-test-ci').all()), 0)
        with self.assertRaises(requests.HTTPError) as err:
            Drone.Secrets('foobar', 'orara').all()
            self.assertEqual(err.response.status_code, 404)

    def test_info(self):
        with  self.assertRaises(requests.HTTPError) as err:
            Drone.Secrets('tinvaan', 'drone-test-ci').info('foo')
            self.assertEqual(404, err.response.status_code)

    def test_create(self):
        self.assertEqual(self.secret.get('name'), 'Testsecret')
        self.assertListEqual(list(self.secret.keys()), ['id', 'repo_id', 'name'])
        with self.assertRaises(requests.HTTPError) as err:
            kwargs = {
                'name': 'Testsecret', 'data': 'This is a test', 'pull_request': False
            }
            Drone.Secrets('tinvaan', 'drone-test-ci').create(**kwargs)
            self.assertTupleEqual(err.response.json(), 404)

            secret.update({'name': 'Test secret'})
            Drone.Secrets('tinvaan', 'drone-test-ci').create(**kwargs)
            self.assertTupleEqual(
                err.response.json(), {"message": "Invalid Secret Name"})

            secret.pop('data')
            Drone.Secrets('tinvaan', 'drone-test-ci').create(**kwargs)
            self.assertTupleEqual(
                err.response.json(), {"message": "Invalid Secret Value"})

    def test_update(self):
        kwargs = {'data': 'This is an updated test'}
        secrets = Drone.Secrets('tinvaan', 'drone-test-ci')
        response = secrets.update(self.secret.get('name'), **kwargs)
        self.assertEqual(
            list(response.keys()), ['id', 'repo_id', 'name'])
        with self.assertRaises(requests.HTTPError) as err:
            secrets.update('foobar', **kwargs)
            self.assertEqual(err.response.status_code, 404)

    def test_delete(self):
        self.assertEqual(
            Drone.Secrets('tinvaan', 'drone-test-ci').delete(self.secret.get('name')), '')
        with self.assertRaises(requests.HTTPError) as err:
            Drone.Secrets('tinvaan', 'drone-test-ci').delete('foobar')
            self.assertEqual(err.response.status_code, 404)

    def tearDown(self):
        for secret in Drone.Secrets('tinvaan', 'drone-test-ci').all():
            Drone.Secrets('tinvaan', 'drone-test-ci').delete(secret.get('name'))


if __name__ == '__main__':
    unittest.main()
