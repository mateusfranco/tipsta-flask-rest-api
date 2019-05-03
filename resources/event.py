from flask_restful import Resource
from flask.json import jsonify
from flask import request
from datetime import datetime

from auxliar import data_json,verify_token
from app.models import Event
from app import db, redis

class Event_All(Resource):

    def get(self):
        events = Event.query.all()
        events_show = []
        for i in events:
            event = {
                "name" : i.name,
                "location" : i.location,
                "coverage_area" : i.coverage_area,
                "date_start" : i.date_start,
                "date_end" : i.date_end,
                "description": i.description,
                "coordinator": i.coordinator  
            }
            events_show.append(event)
        return jsonify(events_show)

    def post(self):
        json_data = data_json()
        if(not verify_token(json_data)):
            return jsonify({"message":"token incorrect"})
        aux_data = json_data["date_start"].split("-")
        date_start = datetime(int(aux_data[0]), int(aux_data[1]), int(aux_data[2]))
        aux_data = json_data["date_end"].split("-")
        date_end = datetime(int(aux_data[0]), int(aux_data[1]), int(aux_data[2]))
        
        event = Event(name = json_data["name"],
                        location = json_data["location"],
                        coverage_area = json_data["coverage_area"],
                        date_start = date_start,
                        date_end = date_end,
                        description = json_data["description"],
                        coordinator = json_data["coordinator"]
                        )
        db.session.add(event)
        db.session.commit()
        return 200

    def put(self):
        json_data = data_json()
        if(not verify_token(json_data)):
            return jsonify({"message":"token incorrect"})
        event = Event.query.filter_by(name=json_data["name"]).first()
        if(json_data["new_name"]):
            event.name = json_data["new_name"]
        event.location = json_data["location"]
        event.coverage_area =  json_data["coverage_area"]
        event.date_start = json_data["date_start"]
        event.date_end = json_data["date_end"]
        event.description = json_data["description"]
        event.coordinator = json_data["coordinator"]
        db.session.add(event)
        db.session.commit()
        return 200

    def delete(self):
        json_data = data_json()
        if(not verify_token(json_data)):
            return jsonify({"message":"token incorrect"})
        event = Event.query.filter_by(name_event=json_data["name"]).first()
        if(event.event_coordinato == json_data["email"]):
            db.session.delete(event)
            db.session.commit()
            return 200
        return jsonify({"error":"voce nao e o cooredenador do evento"}), 400

        