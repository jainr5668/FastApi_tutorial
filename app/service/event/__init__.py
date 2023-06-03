from fastapi.responses import JSONResponse
from app.database.event import EventPostModel, EventGetAllSchema


class EventService:
    def __init__(self, db):
        self.__db = db

    def get_all_events(self):
        events = self.__db().query(EventPostModel).all()
        # open('ronak.log','w').write(events)
        response = EventGetAllSchema(length=len(events),data=events)
        return response
    
        
    def create_event(self, request):
        event = EventPostModel(name=request.name, description=request.description)
        self.__update_database(event)
        return {"id":event.id,"data":event}
    
    
    def get_event(self, id):
        event = self.__db().query(EventPostModel).filter(EventPostModel.id == id).first()
        if not event:
            return self.__response_404()
        event = event.first()
        return event
    
    def update_event(self, id):
        event = self.__db().query(EventPostModel).filter(EventPostModel.id == id).first()
        if not event:
            return self.__response_404()
        for var, value in vars(EventPostModel).items():
            setattr(event, var, value) if value else None

        self.__update_database(event)
        return event

    def __update_database(self, event):
        db = self.__db()
        db.add(event)
        db.commit()
        db.refresh(event)

    def __response_404(self):
        return JSONResponse(content = {'status' : '0'}, status_code=404)