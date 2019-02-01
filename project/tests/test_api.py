# project/server/tests/test_user.py


import datetime
import unittest


from base import BaseTestCase


class TestApiBlueprint(BaseTestCase):
    def test_about_page(self):
        with self.client:
            response = self.client.get("/about")
            self.assertIn(b"name", response.data)
            self.assertIn(b"version", response.data)


if __name__ == "__main__":
    unittest.main()
