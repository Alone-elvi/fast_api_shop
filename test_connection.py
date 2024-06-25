from sqlalchemy import text
from db_connection import engine

def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        for row in result:
            print(row)

if __name__ == "__main__":
    test_connection()