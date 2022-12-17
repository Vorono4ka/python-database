import atexit

from .test_database import TestDatabase

test_database = TestDatabase()


def close_all_databases():
    test_database.close()


atexit.register(close_all_databases)
