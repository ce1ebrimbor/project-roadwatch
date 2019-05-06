# project/server/tests/test_user.py

from base import BaseTestCase
import unittest


class TestUser(BaseTestCase):

    def test_home_page(self):
        with self.client:
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)

    def test_doc_page(self):
        with self.client:
            response = self.client.get("/docs")
            self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        with self.client:
            response = self.client.get("/aboutpage")
            self.assertEqual(response.status_code, 200)
