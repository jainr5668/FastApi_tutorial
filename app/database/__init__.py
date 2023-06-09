from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()


class Database:
    __DATABASE_PATH = 'sqlite:///./event.db'
    __connect_args = {"check_same_thread": False}
    __engine = create_engine(__DATABASE_PATH,
                             connect_args=__connect_args)
    __session_local = None

    @property
    def session_local(self):
        if self.__session_local is None:
            self.__session_local = sessionmaker(
                bind=self.__engine, autoflush=False,
                autocommit=False)
            base.metadata.create_all(bind=self.__engine)
        return self.__session_local
