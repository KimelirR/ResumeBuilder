import time
from sqlmodel import create_engine, SQLModel, Session
from pydantic import BaseSettings

class Settings(BaseSettings):
    db_connection_str: str

settings = Settings()

engine = create_engine(settings.db_connection_str, echo=True)

def initialize_db():
    time.sleep(5)
    SQLModel.metadata.create_all(bind=engine)

def get_db_session():
    with Session(engine) as session:
        yield session


