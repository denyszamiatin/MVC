import csv


class Serializer:
    def __init__(self, filename='contacts.csv'):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, 'rt') as f:
                reader = csv.reader(f)
                return {name: phone for name, phone in reader}
        except FileNotFoundError:
            return {}

    def save(self, data):
        with open(self.filename, 'wt') as f:
            writer = csv.writer(f)
            for name, phone in data.items():
                writer.writerow((name, phone))