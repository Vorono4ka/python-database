import atexit

from .example_database import ExampleDatabase

example_database = ExampleDatabase()


def close_all_databases():
    example_database.close()


atexit.register(close_all_databases)
