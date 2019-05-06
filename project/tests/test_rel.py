# project/server/tests/test_id.py

from base import BaseTestCase
import unittest


class TestRelationships(BaseTestCase):

    def __test_relationship(self, type, id, related_type):
        with self.client:
            response = self.client.get("/{0}/{1}/relationships/{2}".format(type, id, related_type))
            self.assertIn(bytes("\"type\": \"{0}\"".format(related_type), 'utf-8'), response.data)
            self.assertIn(bytes("\"self\": \"/{0}/{1}/relationships/{2}\"".format(type, id, related_type), 'utf-8'), response.data)
            self.assertEqual(response.status_code, 200)


    def test_accident_lieu(self):
        self.__test_relationship("accident", "201700000001", "lieu")

    def test_accident_usager(self):
        self.__test_relationship("accident", "201700000001", "usager")

    def test_accident_vehicule(self):
        self.__test_relationship("accident", "201700000001", "vehicule")

    def test_lieu_accident(self):
        self.__test_relationship("lieu", "1", "accident")

    def test_usager_accident(self):
        self.__test_relationship("usager", "1", "accident")

    def test_vehicule_accident(self):
        self.__test_relationship("vehicule", "1", "accident" )

    def test_departement_accident(self):
        self.__test_relationship("departement", "590", "accident")


if __name__ == "__main__":
    unittest.main()
