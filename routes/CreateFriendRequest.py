from flask import Blueprint, request, jsonify
from database.database import db
import uuid
from flask_cors import CORS, cross_origin


createFriendRequest = Blueprint("createFriendRequest", __name__)
CORS(createFriendRequest)

@createFriendRequest.route("/api/friend/request", methods=["POST"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def createFriendRequestRoute():
  data = request.get_json()

  if not data:
    return (jsonify({"error": "Missing data"}), 400)

  userId = data.get("userId")
  firstName = data.get("firstName")
  lastName = data.get("lastName")
  fullName = data.get("fullName")
  imageUrl = data.get("imageUrl")
  friendId = data.get("friendId")
  friendFirstName = data.get("friendFirstName")
  friendLastName = data.get("friendLastName")
  friendFullName = data.get("friendFullName")
  friendImageUrl = data.get("friendImageUrl")
  
  error_log = {
    "userId":userId,
    "firstName":firstName,
    "lastName":lastName,
    "fullName": fullName,
    "imageUrl":imageUrl,
    "friendId":friendId,
    "friendFirstName":friendFirstName,
    "friendLastName":friendLastName,
    "friendFullName": friendFullName,
    "friendImageUrl":friendImageUrl,
  }

  for key in error_log:
    if not error_log[key]:
      return (jsonify({"error": "Missing {}".format(key)}), 400)
  
  if userId == friendId:
    return (jsonify({"error": "Cannot friend self"}), 400)

  
  requestId = str(uuid.uuid4())
  data["requestId"] = requestId

  db.collection("Request").document(requestId).set(data)
  return {"request": data}