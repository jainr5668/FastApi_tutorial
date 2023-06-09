import copy
from fastapi.responses import JSONResponse
from app.database.game import GamePostModel, GameGetAllSchema


class GameService:
    def __init__(self, db):
        self.__db = db

    def get_all_games(self) -> GameGetAllSchema:
        games = self.__db().query(GamePostModel).all()
        response = GameGetAllSchema(length=len(games), data=games)
        return response

    def create_game(self, request):
        event = GamePostModel(
            name=request.name,
            description=request.description,
            no_of_players=request.no_of_players,
            is_indoor=request.is_indoor,
            is_team_game=request.is_team_game)
        db = self.__db()
        db.add(event)
        db.commit()
        db.refresh(event)
        return {"id": event.id, "data": event}

    def get_game(self, id):
        event = self.__db().query(GamePostModel).filter(
            GamePostModel.id == id).all()
        if not event:
            return JSONResponse(content={'status': f'Game with the id: {id} does not exists.'}, status_code=404)
        event = event[0]
        return {"id": event.id, "data": event}

    def update_game(self, request):
        db = self.__db()
        event = db.query(GamePostModel).filter(
            GamePostModel.id == request.id).first()
        if not event:
            return JSONResponse(content={'status': f'Game with the id: {request.id} does not exists.'}, status_code=404)
        for name, value in request:
            setattr(event,name,value) if value else None
        db.add(event)
        db.commit()
        db.refresh(event)
        return {"id": event.id, "data": event}

