# project/server/tests/test_user.py


import unittest
from base import BaseTestCase


class TestApiBlueprint(BaseTestCase):
    def test_about_page(self):
        with self.client:
            response = self.client.get("/about")
            self.assertIn(b"name", response.data)
            self.assertIn(b"version", response.data)

    def test_accident_list(self):
        with self.client:
            response = self.client.get("/accident")
            self.assertIn(b"\"type\": \"accident\"", response.data)
            self.assertIn(b"usager", response.data)
            self.assertIn(b"lieu", response.data)
            self.assertIn(b"vehicule", response.data)

    def test_usager_list(self):
        with self.client:
            response = self.client.get("/usager")
            self.assertIn(b"\"type\": \"usager\"", response.data)
            self.assertIn(b"relationships", response.data)
            self.assertIn(b"accident", response.data)

    def test_lieu_list(self):
        with self.client:
            response = self.client.get("/lieu")
            self.assertIn(b"\"type\": \"lieu\"", response.data)
            self.assertIn(b"relationships", response.data)
            self.assertIn(b"accident", response.data)

    def test_vehicule_list(self):
        with self.client:
            response = self.client.get("/vehicule")
            self.assertIn(b"\"type\": \"vehicule\"", response.data)
            self.assertIn(b"relationships", response.data)
            self.assertIn(b"accident", response.data)


if __name__ == "__main__":
    unittest.main()
