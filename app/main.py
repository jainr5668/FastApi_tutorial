from fastapi import FastAPI
from app.api import Api

app = FastAPI()

api_routes = Api()
app.include_router(api_routes.router)
@app.route('/')
def root():
    return {'message': 'Hello World'}