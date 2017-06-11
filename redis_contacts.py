from abstact_contacts import AbstractContacts
import redis


class Contacts(AbstractContacts):
    r = redis.StrictRedis()

    def _read_contact(self, name):
        return self.r.get('phones:' + name)

    def read_contact(self, name):
        phone = self._read_contact(name)
        if not phone:
            raise ValueError("Contact doesn't exist")
        return phone.decode('utf8')

    def create_contact(self, name, phone):
        if not self._read_contact(name):
            self.r.set("phones:" + name, phone)
        else:
            raise ValueError("Contact exists")

    def delete_contact(self, name):
        if self._read_contact(name):
            self.r.delete("phones:" + name)
        else:
            raise ValueError("Contact doesn't exist")

    def update_contact(self, name, phone):
        if self._read_contact(name):
            self.r.set("phones:" + name, phone)
        else:
            raise ValueError("Contact doesn't exist")
