from flask_restful import Resource
from flask.json import jsonify
from flask import request
from datetime import datetime

from app.models import Event,Trail
from app import db, redis
from auxliar import verify_token, data_json


class Trail_crud(Resource):
    def get(self):
        json_data = data_json()
        trails = []
        search_trails = Trail.query.all()
        for i in search_trails:
            trail={
                "name" : i.name,
                "date_start" : i.date_start,
                "date_end" : i.date_end,
                "coordinator" : i.coordinator,
                "event" : i.belong,
                "checklist" : i.checklist,
                "appraiser" : i.appraiser
            }
            trails.append(trail)
        for i in search_trails:
            data = {
                "name" : i.name,
                "trail" : trails[i]
            }
        return jsonify(data)
        
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass

class Trail_search(Resource):
    def get(self, event):
        json_data = data_json()
        if(not verify_token(json_data)):
            return jsonify({"message":"token incorrect"})
        event = Event.query.filter_by(name=json_data[event])
        for i in event.trail:
            pass