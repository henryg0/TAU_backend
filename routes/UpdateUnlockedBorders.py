from flask import Blueprint, request, jsonify
from database.database import db
from firebase_admin import exceptions, firestore
from flask_cors import CORS, cross_origin


updateUnlockedBorders = Blueprint("updateUnlockedBorders", __name__)
CORS(updateUnlockedBorders)

@updateUnlockedBorders.route("/api/user/<userId>/unlocked/borders/update", methods = ["PUT"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def updateUnlockedBordersRoute(userId):
  data = request.get_json()

  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)

  if not data:
    return (jsonify({"msg": "Missing data"}), 400)

  unlockedBorders = data.get("unlockedBorders")

  error_log = {
    "unlockedBorders": unlockedBorders,
  }

  for key in error_log:
    if not error_log.get(key):
      return (jsonify({"error": "Missing {}".format(key)}), 400)
  
  newUnlockedBorders = data.get("unlockedBorders")
  user = db.collection('Users').where("userId", "==", userId).stream()
  oldUnlockedBorders = [doc.to_dict() for doc in user][0]["unlockedBorders"]

  fields = {"unlockedBorders.BLACK": True}
  arr = []
  for newBorder in newUnlockedBorders:
    if newBorder not in oldUnlockedBorders:
      fields["unlockedBorders." + newBorder] = True 
      arr.append(newBorder)

  ref = db.collection("Users").document(userId).update(fields)

  return ({"msg": arr})