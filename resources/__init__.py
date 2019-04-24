from event import Event_All
from flask_restful import Api

def init_resources(app):
    api = Api(app)
    return app