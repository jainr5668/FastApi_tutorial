import copy
from fastapi.responses import JSONResponse
from app.database.event import EventPostModel, EventGetAllSchema


class EventService:
    def __init__(self, db):
        self.__db = db

    def get_all_events(self):
        events = self.__db().query(EventPostModel).all()
        response = EventGetAllSchema(length=len(events), data=events)
        return response

    def create_event(self, request):
        event = EventPostModel(
            name=request.name,
            description=request.description,
            start_date=request.start_date,
            end_date=request.end_date,
            max_player=request.max_player,
            min_player=request.min_player)
        db = self.__db()
        db.add(event)
        db.commit()
        db.refresh(event)
        return {"id": event.id, "data": event}

    def get_event(self, id):
        event = self.__db().query(EventPostModel).filter(
            EventPostModel.id == id).all()
        if not event:
            return JSONResponse(content={'status': '0'}, status_code=404)
        event = event[0]
        return event

    def update_event(self, request):
        db = self.__db()
        event = db.query(EventPostModel).filter(
            EventPostModel.id == request.id).first()
        if not event:
            return JSONResponse(content={'status': f'Event with the id: {request.id} does not exists.'}, status_code=404)
        for name, value in request:
            setattr(event,name,value) if value else None
        db.add(event)
        db.commit()
        db.refresh(event)
        return {"id": event.id, "data": event}

