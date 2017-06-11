from abstact_contacts import AbstractContacts
import sqlite3


class Contacts(AbstractContacts):
    db = sqlite3.connect('phones.db')

    def _read_contact(self, name):
        return self.db.execute(
            "select name, phone from phones where name=?",
            (name,)
        ).fetchone()

    def read_contact(self, name):
        row = self._read_contact(name)
        if row:
            return row[1]
        else:
            raise ValueError("Contact doesn't exist")

    def create_contact(self, name, phone):
        row = self._read_contact(name)
        if not row:
            self.db.execute(
                "insert into phones (name, phone) values (?, ?)",
                (name, phone)
            )
        else:
            raise ValueError("Contact exists")

    def delete_contact(self, name):
        row = self._read_contact(name)
        if row:
            self.db.execute(
                "delete from phones where name=?",
                (name,)
            )
        else:
            raise ValueError("Contact doesn't exist")

    def update_contact(self, name, phone):
        row = self._read_contact(name)
        if row:
            self.db.execute(
                "update phones set phone=? where name=?",
                (phone, name)
            )
        else:
            raise ValueError("Contact doesn't exist")