from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

DATABASE_URL = "postgresql://spint2:abirvalg@localhost:5436/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autcommit=False, autoflush=False, bind=engine)


def set_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()