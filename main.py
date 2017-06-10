import configparser


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

config = configparser.ConfigParser()
config.read('settings.conf')
serializer_module = __import__(config['Serializer']['name'])
serializer = serializer_module.Serializer()
contacts = Contacts(serializer)

while True:
    action = input('Action? ').lower()
    if action == 'q':
        break
    elif action == 'c':
        name = input('Name? ')
        phone = input('Phone? ')
        try:
            contacts.create_contact(name, phone)
        except ValueError as e:
            print(e)
    elif action == 'r':
        name = input('Name? ')
        try:
            contacts.read_contact(name)
        except ValueError as e:
            print(e)
    elif action == 'u':
        name = input('Name? ')
        phone = input('Phone? ')
        try:
            contacts.update_contact(name, phone)
        except ValueError as e:
            print(e)
    elif action == 'd':
        name = input('Name? ')
        try:
            contacts.delete_contact(name)
        except ValueError as e:
            print(e)
    else:
        print('Invalid action')
