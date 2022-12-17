from datetime import datetime

from .database import Database


class TestDatabase(Database):
    def __init__(self):
        super().__init__(f'./{"databases/" if __name__ != "__main__" else ""}accounts.db')

        self.execute("""CREATE TABLE IF NOT EXISTS test (
            `id` INTEGER PRIMARY KEY NOT NULL
            `create_timestamp` INTEGER NOT NULL
        )""")

    def create(self, id_: int) -> None:
        exists = self.exists('test', 'id', id_)

        if not exists:
            self.insert('test', (
                ('id', id_),
                ('create_timestamp', datetime.utcnow().timestamp())
            ))

            self.commit()

        raise Exception(f'{id_} already exists.')

    def get(self, id_: int) -> tuple or None:
        exists = self.exists('test', 'id', id_)

        if exists:
            account_data = self.select('test', None, ('id', id_), 1)[0]

            return account_data
        return None
