from flask import request, Blueprint, jsonify
from database.database import db
from flask_cors import CORS, cross_origin


deleteFriendRequest = Blueprint("deleteFriendRequest", __name__)
CORS(deleteFriendRequest)

@deleteFriendRequest.route("/api/friend/request/<requestId>/delete", methods = ["DELETE"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def deleteFriendRequestRoute(requestId):
  # add a checking method where only user can delete their own todo
  if not requestId:
    return (jsonify({"error": "Missing requestId"}), 400)

  requestInfo = db.collection('Request').document(requestId).get()
  if not requestInfo.exists:
    return (jsonify({"error": "Friend request not found"}), 404)

  db.collection('Request').document(requestId).delete()
  
  return ({"msg": "Friend request deleted"})