from app.service.event import EventService
from app.database import Database


class Service:
    __event = None

    def __init__(self):
        self.__db = Database().session_local

    @property
    def event(self):
        if self.__event is None:
            self.__event = EventService(self.__db)
        return self.__event
