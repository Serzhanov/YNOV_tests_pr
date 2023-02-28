import unittest

import sys

sys.path.insert(0, "../../../app/")

from people import delete
from app import app
from werkzeug.test import Client

# DATA BASE TESTING

# class TestApp(unittest.TestCase):

#     def setUp(self):
#         self.personObjCreate = {
#                     "fname": "Doe",
#                     "lname": "John create"
#                     }
#         self.personObjDelete = {
#                     "fname": "Doe",
#                     "lname": "John delete"
#                     }
#         self.personObjRead = {
#                     "fname": "Doe",
#                     "lname": "John read"
#                     }
#         self.personObjUpdate = {
#                     "fname": "Doe",
#                     "lname": "John update"
#                     }
#         #delete("John delete")
#         #delete("John update")
#         #delete("John create")
#         #delete("John read")


#     def tearDown(self):

#         delete("John update")
#         delete("John create")
#         delete("John read")
#         delete("John delete")

#         pass

#     def test_create_person(self):
#         person = create(self.personObjCreate)[0]

#         self.assertEqual(person.get('lname'), "John create")
#         self.assertEqual(person.get('fname'), "Doe")

#     def test_read_one(self):
#         person = create(self.personObjRead)[0]
#         result = read_one('John read')
#         self.assertEqual(result.get('lname'), self.personObjRead.get('lname'))

#     def test_update_person(self):
#         person = create(self.personObjUpdate)[0]
#         personObjUpdate2 = {
#                     "fname": "Doe2",
#                     "lname": "John update2"
#                     }
#         updated_person = update('John update', personObjUpdate2)[0]
#         self.assertEqual(updated_person.get('fname'), personObjUpdate2.get('fname'))

#     def test_delete_person(self):
#         person = create(self.personObjDelete)[0]
#         result = delete("John delete")[0]
#         #Checking deleting
#         self.assertEqual(result.get('lname'),"John delete")


# API TESTING


class PeopleCRUDTest(unittest.TestCase):
    def setUp(self):
        # app = config.connex_app
        # app.add_api(config.basedir / "swagger.yml")
        self.client = Client(app)

        self.personObjCreate = {"fname": "RUSLAN", "lname": "BRATAN create"}
        self.personObjDelete = {"fname": "RUSLAN", "lname": "BRATAN delete"}
        self.personObjRead = {"fname": "RUSLAN", "lname": "BRATAN read"}
        self.personObjUpdate = {"fname": "RUSLAN", "lname": "BRATAN update"}

    def tearDown(self):
        delete("BRATAN update")
        delete("BRATAN create")
        delete("BRATAN read")
        # delete("BRATAN delete")

        pass

    def test_create_person(self):
        data = self.personObjCreate
        response = self.client.post("api/people", json=data)
        self.assertEqual(response.status_code, 201)

    def test_read_person(self):
        lname = self.personObjRead["lname"]
        data = self.personObjRead
        self.client.post("api/people", json=data)
        response = self.client.get(f"api/people/{lname}")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["lname"], lname)

    def test_update_person(self):
        lname = self.personObjUpdate["lname"]
        data = self.personObjUpdate
        fname = "RUSLAN UPDATED"
        data["fname"] = fname
        self.client.post("api/people", json=data)
        response = self.client.put(f"api/people/{lname}", json=data)
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["fname"], fname)

    def test_delete_person(self):
        lname = self.personObjDelete["lname"]
        data = self.personObjDelete
        self.client.post("api/people", json=data)
        response = self.client.delete(f"api/people/{lname}")
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
