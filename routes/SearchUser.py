from flask import Blueprint, request, jsonify
from database.database import db
from flask_cors import CORS, cross_origin


searchUser = Blueprint("searchUser", __name__)
CORS(searchUser)

@searchUser.route("/api/user/search", methods = ["GET"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def searchUserRoute():
  email = request.args.get("email")

  if not email:
    return (jsonify({"error": "Missing email"}), 400)

  docs = db.collection('Users')
  result = docs.where("email", "==", email).stream()
  
  
  for doc in result:
    return {"user": doc.to_dict()}

  return (jsonify({"error": "User does not exist"}), 404)
