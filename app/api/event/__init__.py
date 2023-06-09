from fastapi import APIRouter
from app.database.event import EventPostSchema, EventPostResponseSchema
from app.database.event import EventPostSchemaUpdated, EventGetAllSchema
from app.database.event import EventPatchSchema
from app.service import Service


class EventApi:
    __router = None

    def __init__(self, service: Service) -> None:
        self.__service = service

    @property
    def router(self):
        if self.__router is None:
            self.__router = APIRouter(prefix='/events', tags=['Event'])
            self.__get_routes()
        return self.__router

    def __get_routes(self):
        @self.__router.get('/')
        def get_all_events() -> EventGetAllSchema:
            return self.__service.event.get_all_events()

        @self.router.post('/')
        def create_event(request: EventPostSchema) -> EventPostResponseSchema:
            return self.__service.event.create_event(request)

        @self.router.get('/{id}')
        def get_event(id: int) -> EventPostSchemaUpdated:
            return self.__service.event.get_event(id)

        @self.router.patch('/{id}')
        def update_event(request: EventPatchSchema) -> EventPostResponseSchema:
            return self.__service.event.update_event(request)
