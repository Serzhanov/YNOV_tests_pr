import unittest

import sys

sys.path.insert(0, "../../../app/")

from people import create, read_one, update, delete,Person

class TestApp(unittest.TestCase):

    def setUp(self):
        self.personObjCreate = {
                    "fname": "Doe",
                    "lname": "John create"
                    }
        self.personObjDelete = {
                    "fname": "Doe",
                    "lname": "John delete"
                    }
        self.personObjRead = {
                    "fname": "Doe",
                    "lname": "John read"
                    }
        self.personObjUpdate = {
                    "fname": "Doe",
                    "lname": "John update"
                    }
        #delete("John delete")
        #delete("John update")
        #delete("John create")
        #delete("John read")
     

    def tearDown(self):
        
        delete("John update")
        delete("John create")
        delete("John read")
        delete("John delete")
        pass

    def test_create_person(self):
        person = create(self.personObjCreate)[0]

        self.assertEqual(person.get('lname'), "John create")
        self.assertEqual(person.get('fname'), "Doe")

    def test_read_one(self):
        person = create(self.personObjRead)[0]
        result = read_one('John read')
        self.assertEqual(result.get('lname'), self.personObjRead.get('lname'))

    def test_update_person(self):
        person = create(self.personObjUpdate)[0]
        personObjUpdate2 = {
                    "fname": "Doe2",
                    "lname": "John update2"
                    }
        updated_person = update('John update', personObjUpdate2)[0]
        self.assertEqual(updated_person.get('fname'), personObjUpdate2.get('fname'))

    def test_delete_person(self):
        person = create(self.personObjDelete)[0]
        result = delete("John update")[0]
        #Checking deleting
        self.assertEqual(result.get('lname'),"John delete")

if __name__ == '__main__':
    unittest.main()
