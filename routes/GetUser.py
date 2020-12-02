from flask import Blueprint, request, jsonify
from database.database import db
from flask_cors import CORS, cross_origin


getUser = Blueprint("getUser", __name__)
CORs(getUser)

@getUser.route("/api/user/<userId>", methods = ["GET"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def getUserRoute(userId):
  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)
  
  docs = db.collection('Users')
  result = docs.where("userId", "==", userId).stream()

  for doc in result:
    return ({"user": doc.to_dict()})

  return (jsonify({"error": "User does not exist"}), 404)
