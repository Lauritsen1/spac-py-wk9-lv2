import sqlite3

from .singleton_meta import SingletonMeta


class Connection(metaclass=SingletonMeta):
    def __init__(self, db_name=None):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        if self.db_name:
            self.connect()

    def connect(self, db_name=None) -> None:
        if db_name:
            self.db_name = db_name
        if self.db_name and not self.connection:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()

    def disconnect(self) -> None:
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def is_connected(self) -> bool:
        return self.connection is not None
