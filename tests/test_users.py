
import unittest

from requests.exceptions import HTTPError

from drone.users import Drone


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.users = Drone.Users()

    def test_all(self):
        with self.assertRaises(HTTPError) as err:
            self.users.all()
            self.assertEqual(err.response.status_code, 403)

    def test_info(self):
        with self.assertRaises(HTTPError) as err:
            self.users.info(user='tinvaan')
            self.assertEqual(err.response.status_code, 403)

    def test_delete(self):
        with self.assertRaises(HTTPError) as err:
            self.users.delete('tinvaan')
            self.assertEqual(err.response.status_code, 403)

    def test_create(self):
        with self.assertRaises(HTTPError) as err:
            user = {
                "login": "octocat",
                "email": "octocat@github.com",
                "avatar_url": "http://www.gravatar.com/avatar/7194e8d48fa1d2b689f99443b767316c",
                "active": True
            }
            self.users.create(**user)
            self.assertEqual(err.response.status_code, 403)
    
    def test_update(self):
        with self.assertRaises(HTTPError) as err:
            user = {
                "login": "foobar",
                "email": "foobar@github.com",
                "avatar_url": "http://www.gravatar.com/avatar/7194e8d48fa1d2b689f99443b767316c",
                "active": False
            }
            self.users.update('tinvaan', **user)
            self.assertEqual(err.response.status_code, 403)


if __name__ == '__main__':
    unittest.main()
