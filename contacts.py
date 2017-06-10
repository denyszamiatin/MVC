class Contacts:
    def __init__(self, serializer):
        self.serializer = serializer
        self.contacts = self.serializer.load().copy()

    def create_contact(self, name, phone):
        if name not in self.contacts:
            self.contacts[name] = phone
            self.serializer.save(self.contacts)
        else:
            raise ValueError('Contact exists')

    def read_contact(self, name):
        try:
            print(self.contacts[name])
        except KeyError:
            raise ValueError("Contact doesn't exist")

    def update_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
            self.serializer.save(self.contacts)
        else:
            raise ValueError("Contact doesn't exist")

    def delete_contact(self, name):
        try:
            del self.contacts[name]
            self.serializer.save(self.contacts)
        except KeyError:
            raise ValueError("Contact doesn't exist")
