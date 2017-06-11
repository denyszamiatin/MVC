from abstact_contacts import AbstractContacts
import pymongo


class Contacts(AbstractContacts):
    m = pymongo.MongoClient()
    contacts = m.phones.contacts

    def _read_contact(self, name):
        return self.contacts.find_one({"name": name})

    def read_contact(self, name):
        contact = self._read_contact(name)
        if contact:
            return contact['phone']
        raise ValueError("Contact doesn't exist")

    def create_contact(self, name, phone):
        contact = self._read_contact(name)
        if not contact:
            self.contacts.insert_one({'name': name, 'phone': phone})
        else:
            raise ValueError("Contact exists")

    def delete_contact(self, name):
        contact = self._read_contact(name)
        if contact:
            self.contacts.delete_one({'name': name})
        else:
            raise ValueError("Contact doesn't exist")

    def update_contact(self, name, phone):
        contact = self._read_contact(name)
        if contact:
            self.contacts.update_one({'name': name}, {'$set': {'phone': phone}})
        else:
            raise ValueError("Contact doesn't exist")