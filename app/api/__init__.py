

from fastapi import APIRouter

from app.api.event import EventApi
from app.api.game import GameApi
from app.service import Service


class Api:
    __router = None

    def __init__(self) -> None:
        self.__routers = {
            "/ews/v1": [EventApi, GameApi],
        }
        self.__service = Service()

    @property
    def router(self):
        if self.__router is None:
            self.__router = APIRouter()
            self.__get_router()
        return self.__router

    def __get_router(self):
        for key in self.__routers.keys():
            routes = APIRouter(prefix=key)
            for router in self.__routers[key]:
                service_obj = router(self.__service)
                routes.include_router(service_obj.router)
            self.__router.include_router(routes)
