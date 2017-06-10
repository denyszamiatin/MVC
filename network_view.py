import socket


class View:
    def __init__(self):
        s = socket.socket()
        s.bind(('127.0.0.1', 8000))
        s.listen(1)
        self.c, a = s.accept()

    def _print(self, message):
        self.c.sendall(message.encode('utf8'))

    def print(self, message):
        self._print(str(message) + '\n')

    def input(self, message):
        self._print(message)
        return self.c.recv(1024).decode('utf8')[:-2]