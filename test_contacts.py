import unittest

import contacts
import dummy_serializer


class TestContacts(unittest.TestCase):
    def setUp(self):
        self.c = contacts.Contacts(dummy_serializer.Serializer())
        self.c.create_contact('Bill', '1234')

    def test_create(self):
        self.assertEqual(self.c.read_contact('Bill'), '1234')

    def test_update(self):
        self.c.update_contact('Bill', '2234')
        self.assertEqual(self.c.read_contact('Bill'), '2234')