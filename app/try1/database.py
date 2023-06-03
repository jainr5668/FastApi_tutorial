from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_PATH = 'sqlite:///./event.db'
Base = declarative_base()
engine = create_engine(DATABASE_PATH, connect_args={"check_same_thread":False})


session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False)