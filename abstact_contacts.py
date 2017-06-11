from abc import abstractmethod, ABCMeta


class AbstractContacts(metaclass=ABCMeta):
    def __init__(self, serializer):
        pass

    @abstractmethod
    def create_contact(self, name, phone):
        pass

    @abstractmethod
    def read_contact(self, name):
        pass

    @abstractmethod
    def update_contact(self, name, phone):
        pass

    @abstractmethod
    def delete_contact(self, name):
        pass