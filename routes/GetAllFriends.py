from flask import request, Blueprint, jsonify
from database.database import db
from flask_cors import CORS, cross_origin


getAllFriends = Blueprint("getAllFriends", __name__)
CORS(getAllFriends)

@getAllFriends.route("/api/user/<userId>/friend", methods = ["GET"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def getAllFriendsRoute(userId):
  # add a checking method where only user can accept their own todo
  if not userId:
    return (jsonify({"error": "Missing requestId"}), 400)

  docs = db.collection('Friends')
  result = docs.where("userId", "==", userId).stream()
  res = [doc.to_dict() for doc in result]
  return {"friends": res}