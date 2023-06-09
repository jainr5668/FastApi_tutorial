from app.service.event import EventService
from app.database import Database
from app.service.game import GameService


class Service:
    __event = None
    __game = None

    def __init__(self):
        self.__db = Database().session_local

    @property
    def event(self):
        if self.__event is None:
            self.__event = EventService(self.__db)
        return self.__event


    @property
    def game(self):
        if self.__game is None:
            self.__game = GameService(self.__db)
        return self.__game
