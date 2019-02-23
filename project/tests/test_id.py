# project/server/tests/test_id.py

from base import BaseTestCase
import unittest


class TestGetById(BaseTestCase):

    def __test_id(self, type, id):
        with self.client:
            response = self.client.get("/{0}/{1}".format(type, id))
            self.assertIn(bytes("\"type\": \"{0}\"".format(type), 'ascii'), response.data)
            self.assertIn(bytes("\"id\": {0}".format(id), 'ascii'), response.data)
            self.assertEqual(response.status_code, 200)


    def test_accident_id(self):
        self.__test_id("accident", "201700000001")

    def test_usager_id(self):
        self.__test_id("usager", "1")

    def test_vehicule_id(self):
        self.__test_id("vehicule", "1")

    def test_lieu_id(self):
        self.__test_id("usager", "1")

if __name__ == "__main__":
    unittest.main()
