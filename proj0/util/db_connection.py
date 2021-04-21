import psycopg2
from psycopg2._psycopg import OperationalError


def create_connection():
    try:
        # deleted credentials for github
        conn = psycopg2.connect()
        return conn
    except OperationalError as e:
        print(f"{e}")
        return conn


connection = create_connection()
