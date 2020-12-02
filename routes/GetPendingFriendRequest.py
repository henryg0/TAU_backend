from flask import request, Blueprint, jsonify
from database.database import db
from flask_cors import CORS, cross_origin



getPendingFriendRequest = Blueprint("getPendingFriendRequest", __name__)
CORS(getPendingFriendRequest)

@getPendingFriendRequest.route("/api/user/<userId>/friend/pending", methods=["GET"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def getPendingFriendRequestRoute(userId):
  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)
  
  docs = db.collection('Request')
  result = docs.where("userId", "==", userId).stream()
  res = [doc.to_dict() for doc in result]
  
  return {"pending" : res}