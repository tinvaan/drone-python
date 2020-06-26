
import requests
import unittest

from drone.drone import Drone


class TestCron(unittest.TestCase):
    def setUp(self):
        self.cron = Drone.Cron('tinvaan', 'drone-test-ci')
        self.cron.create(**{
            'name': 'nightly', 'expr': '0 0 1 * * *', 'branch': 'master' })

    def test_all(self):
        self.assertGreater(len(self.cron.all()), 0) 

    def test_info(self):
        response = self.cron.info('nightly')
        self.assertTrue(isinstance(response, dict))
        self.assertEqual(list(response.keys()), [
            'id', 'repo_id', 'name', 'expr', 'next', 'prev', 'event', 'branch',
            'disabled', 'created', 'updated', 'version'])
        with self.assertRaises(requests.HTTPError) as err:
            self.cron.info('foobar')
            self.assertEqual(err.response.status_code, 404)

    def test_create(self):
        kwargs = {
            'name': 'nightly2', 'expr': '0 0 1 * * *', 'branch': 'master' }
        response = self.cron.create(**kwargs)
        self.assertTrue(isinstance(response, dict))
        self.assertListEqual(list(response.keys()), [
            'id', 'repo_id', 'name', 'expr', 'next', 'prev', 'event', 'branch',
            'disabled', 'created', 'updated', 'version'])

    def test_delete(self):
        self.assertEqual(self.cron.delete('nightly'), '')
        with self.assertRaises(requests.HTTPError) as err:
            self.cron.delete('foobar')
            self.assertEqual(err.response.status_code, 404)

    def test_update(self):
        kwargs = {
            'name': 'nightly', 'expr': '0 0 1 * * *', 'branch': 'master' }
        response = self.cron.update('nightly', **kwargs)
        self.assertTrue(isinstance(response, dict))
        self.assertEqual(response.get('branch'), 'master')

        kwargs.update({'branch': 'development'})
        response = self.cron.update('nightly', **kwargs)
        self.assertTrue(isinstance(response, dict))
        self.assertEqual(response.get('branch'), 'development')

        with self.assertRaises(requests.HTTPError) as err:
            self.cron.update('foobar', **kwargs)
            self.assertEqual(err.response.status_code, 404)

    def tearDown(self):
        for cron in self.cron.all():
            self.cron.delete(cron.get('name'))


if __name__ == '__main__':
    unittest.main()
