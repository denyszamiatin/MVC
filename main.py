import configparser


config = configparser.ConfigParser()
config.read('settings.conf')
serializer_module = __import__(config['Serializer']['name'])
serializer = serializer_module.Serializer()
view_module = __import__(config['View']['name'])
view = view_module.View()
model_module = __import__(config['Model']['name'])
contacts = model_module.Contacts(serializer)

while True:
    action = view.input('Action? ').lower()
    if action == 'q':
        break
    elif action == 'c':
        name = view.input('Name? ')
        phone = view.input('Phone? ')
        try:
            contacts.create_contact(name, phone)
        except ValueError as e:
            view.print(e)
    elif action == 'r':
        name = view.input('Name? ')
        try:
            view.print(contacts.read_contact(name))
        except ValueError as e:
            view.print(e)
    elif action == 'u':
        name = view.input('Name? ')
        phone = view.input('Phone? ')
        try:
            contacts.update_contact(name, phone)
        except ValueError as e:
            view.print(e)
    elif action == 'd':
        name = view.input('Name? ')
        try:
            contacts.delete_contact(name)
        except ValueError as e:
            view.print(e)
    else:
        view.print('Invalid action')
