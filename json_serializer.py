import json


class JsonSerializer:
    def __init__(self, filename='contacts.json'):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, 'rt') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save(self, data):
        with open(self.filename, 'wt') as f:
            json.dump(data, f)
