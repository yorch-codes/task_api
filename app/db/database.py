from typing import cast

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load from environments the database url
DATABASE_URL = cast(str, config("DATABASE_URL"))

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Create the session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for declarative models
Base = declarative_base()


def get_db():
    """
    Dependency for getting a database session.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
