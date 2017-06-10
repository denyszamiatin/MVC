class Contacts:
    def __init__(self):
        self.contacts = {}

    def create_contact(self, name, phone):
        if name not in self.contacts:
            self.contacts[name] = phone
        else:
            print('Contact exists')

    def read_contact(self, name):
        try:
            print(self.contacts[name])
        except KeyError:
            print("Contact doesn't exist")

    def update_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
        else:
            print("Contact doesn't exist")

    def delete_contact(self, name):
        try:
            del self.contacts[name]
        except KeyError:
            print("Contact doesn't exist")


contacts = Contacts()
while True:
    action = input('Action? ').lower()
    if action == 'q':
        break
    elif action == 'c':
        name = input('Name? ')
        phone = input('Phone? ')
        contacts.create_contact(name, phone)
    elif action == 'r':
        name = input('Name? ')
        contacts.read_contact(name)
    elif action == 'u':
        name = input('Name? ')
        phone = input('Phone? ')
        contacts.update_contact(name, phone)
    elif action == 'd':
        name = input('Name? ')
        contacts.delete_contact(name)
    else:
        print('Invalid action')
