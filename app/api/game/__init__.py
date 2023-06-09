from fastapi import APIRouter
from app.database.game.game_schema import GameGetAllSchema, GamePatchSchema
from app.database.game.game_schema import  GamePostSchema,GamePostResponseSchema
from app.service import Service


class GameApi:
    __router = None

    def __init__(self, service: Service) -> None:
        self.__service = service

    @property
    def router(self):
        if self.__router is None:
            self.__router = APIRouter(prefix='/games', tags=['Game'])
            self.__get_routes()
        return self.__router

    def __get_routes(self):
        @self.__router.get('/')
        async def get_all_games()-> GameGetAllSchema:
            return self.__service.game.get_all_games()

        @self.router.post('/')
        async def create_game(request: GamePostSchema) -> GamePostResponseSchema:
            return self.__service.game.create_game(request)

        @self.router.get('/{id}')
        async def get_game(id: int) -> GamePostResponseSchema:
            return self.__service.game.get_game(id)

        @self.router.patch('/{id}')
        async def update_game(request: GamePatchSchema) -> GamePostResponseSchema:
            return self.__service.game.update_game(request)
