from flask.json import jsonify
from flask import request

from app import redis

def verify_token(json):
    json_data = request.get_json()
    email = json_data["email"]
    token_verify = json_data["token"]
    token = redis.hget(email, "field1")
    if(token == token_verify):
        return True
    return False

def data_json():
    json_data = request.get_json(force=True)
    if(not json_data):
        return jsonify({'message': 'No input data provided'}), 400   
    return json_data