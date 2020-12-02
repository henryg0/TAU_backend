from flask import request, Blueprint, jsonify
from database.database import db
import uuid
from google.cloud.firestore_v1 import Increment
from flask_cors import CORS, cross_origin



acceptFriendRequest = Blueprint("acceptFriendRequest", __name__)
CORS(acceptFriendRequest)

@acceptFriendRequest.route("/api/friend/request/<requestId>/accept", methods = ["POST"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def acceptFriendRequestRoute(requestId):
  # add a checking method where only user can accept their own todo
  if not requestId:
    return (jsonify({"error": "Missing requestId"}), 400)

  requestInfo = db.collection('Request').document(requestId).get()
  if not requestInfo.exists:
    return (jsonify({"error": "Friend request not found"}), 404)
  requestInfo = requestInfo.to_dict()

  userFriendIdOne = str(uuid.uuid4())
  userFriendIdTwo = str(uuid.uuid4())
  userData = {
    "userId": requestInfo["userId"],
    "fullName": requestInfo["friendFullName"],
    "firstName": requestInfo["friendFirstName"],
    "lastName": requestInfo["friendLastName"],
    "imageUrl": requestInfo["friendImageUrl"],
    "friendId": requestInfo["friendId"],
    "userFriendIdOne": userFriendIdOne,
    "userFriendIdTwo": userFriendIdTwo
  }

  db.collection("Friends").document(userFriendIdOne).set(userData)
  db.collection("Users").document(requestInfo["userId"]).update({'friendCount': Increment(1)})

  friendData = {
    "userId": requestInfo["friendId"],
    "fullName": requestInfo["fullName"],
    "firstName": requestInfo["firstName"],
    "lastName": requestInfo["lastName"],
    "imageUrl": requestInfo["imageUrl"],
    "friendId": requestInfo["userId"],
    "userFriendIdTwo": userFriendIdOne,
    "userFriendIdOne": userFriendIdTwo
  }
  db.collection("Friends").document(userFriendIdTwo).set(friendData)
  db.collection("Users").document(requestInfo["friendId"]).update({'friendCount': Increment(1)})
  db.collection('Request').document(requestId).delete()
  
  return ({"friend": friendData})