from flask_restful import Resource
from flask.json import jsonify
from flask import request
from datetime import datetime

from app.models import Event
from app import db, redis

class Event_All(Resource):

    def get(self):
        events = Event.query.all()
        events_show = []
        for i in events:
            event = {
                "name_event" : i.name_event,
                "event_location" : i.event_location,
                "coverage_area" : i.coverage_area,
                "date_start_event" : i.date_start_event,
                "date_end_event" : i.date_end_event,
                "event_description": i.event_description,
                "event_coordinator": i.event_coordinator  
            }
            events_show.append(event)
        return jsonify(events_show)

    def post(self):
        json_data = request.get_json(force=True)
        if(not json_data):
            return jsonify({'message': 'No input data provided'}), 400   
        email = json_data["email"]
        token_verify = json_data["token"]
        token = redis.hget(email, "field1")
        if(token != token_verify):
            return jsonify({'message': 'token wrong'}), 400
        event = Event(name_event = json_data["name_event"],
                        event_location = json_data["event_location"],
                        coverage_area = json_data["coverage_area"],
                        date_start_event = json_data["date_start_event"],
                        date_end_event = json_data["date_end_event"],
                        event_description = json_data["event_description"],
                        event_coordinator = json_data["event_coordinator"]
                        )
        db.session.add(event)
        db.session.commit()
        return 200

    def put(self):
        json_data = request.get_json(force=True)
        if(not json_data):
            return jsonify({'message': 'No input data provided'}), 400   
        email = json_data["email"]
        token_verify = json_data["token"]
        token = redis.hget(email, "field1")
        if(token != token_verify):
            return jsonify({'message': 'token wrong'}), 400
        event = Event.query.filter_by(name_event=json_data["name_event"]).first()
        if(json_data["new_name"]):
            event.name_event = json_data["new_name"]
        event.event_location = json_data["event_location"]
        event.coverage_area =  json_data["coverage_area"]
        event.date_start_event = json_data["date_start_event"]
        event.date_end_event = json_data["date_end_event"]
        event.event_description = json_data["event_description"]
        event.event_coordinator = json_data["event_coordinator"]
        db.session.add(event)
        db.session.commit()

    def delete(self):
        json_data = request.get_json(force=True)
        if(not json_data):
            return jsonify({'message': 'No input data provided'}), 400   
        email = json_data["email"]
        token_verify = json_data["token"]
        token = redis.hget(email, "field1")
        if(token != token_verify):
            return jsonify({'message': 'token wrong'}), 400
        event = Event.query.filter_by(name_event=json_data["name_event"]).first()
        if(event.event_coordinato == email):
            db.session.delete(event)
            db.session.commit()
            return 200
        return jsonify({"error":"voce nao e o cooredenador do evento"}), 400
           
        