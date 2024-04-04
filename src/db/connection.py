import sqlite3

from .singleton_meta import SingletonMeta


class Connection(metaclass=SingletonMeta):
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name, check_same_thread=False)

    def cursor(self):
        return self.connection.cursor()

    def disconnect(self) -> None:
        if self.connection:
            self.connection.close()

    def is_connected(self) -> bool:
        return self.connection is not None
