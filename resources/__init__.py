from event import Event_All
from trail import Trail_crud, Trail_search
from flask_restful import Api

def init_resources(app):
    api = Api(app)
    api.add_resource(Event_All,"/event")
    api.add_resource(Trail_crud,"/trail")
    api.add_resource(Trail_search,"/trail/<event>")
    return app