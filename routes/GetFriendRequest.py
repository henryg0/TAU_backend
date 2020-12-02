from flask import request, Blueprint, jsonify
from database.database import db
from flask_cors import CORS, cross_origin


getFriendRequest = Blueprint("getFriendRequest", __name__)
CORS(getFriendRequest)

@getFriendRequest.route("/api/user/<userId>/friend/request", methods=["GET"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def getFriendRequestRoute(userId):
  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)

  docs = db.collection('Request')
  result = docs.where("friendId", "==", userId).stream()
  
  res = [doc.to_dict() for doc in result]
  
  return {"friends": res}