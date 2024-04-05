from dataclasses import dataclass

from db import Connection

connection = Connection("data/db/Cereal.db")
cur = connection.cursor()


class QueryBuilder:
    def __init__(self):
        self.query = ''
        self.params = []

    def SELECT(self, *columns):
        self.query += f'SELECT {", ".join(columns)} ' if columns else 'SELECT * '
        return self

    def FROM(self, table):
        self.query += f'FROM {table} '
        return self

    def WHERE(self, **kwargs):
        conditions = [f'{k} = ?' for k in kwargs.keys()]
        self.query += f'WHERE {" AND ".join(conditions)} '
        self.params.extend(kwargs.values())
        return self

    def execute(self):
        data = cur.execute(self.query, self.params).fetchall()
        return data


db = QueryBuilder()

data = db.SELECT().FROM('cereals').WHERE(id=2).execute()
