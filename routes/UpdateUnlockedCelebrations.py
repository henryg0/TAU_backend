from flask import Blueprint, request, jsonify
from database.database import db
from firebase_admin import exceptions, firestore
from flask_cors import CORS, cross_origin


updateUnlockedCelebrations = Blueprint("updateUnlockedCelebrations", __name__)
CORS(updateUnlockedCelebrations)

@updateUnlockedCelebrations.route("/api/user/<userId>/unlocked/celebrations/update", methods = ["PUT"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def updateUnlockedCelebrationsRoute(userId):
  data = request.get_json()

  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)

  if not data:
    return (jsonify({"msg": "Missing data"}), 400)

  unlockedCelebrations = data.get("unlockedCelebrations")

  error_log = {
    "unlockedCelebrations": unlockedCelebrations,
  }

  newUnlockedCelebrations = data.get("unlockedCelebrations")
  user = db.collection('Users').where("userId", "==", userId).stream()
  oldUnlockedCelebrations = [doc.to_dict() for doc in user][0]["unlockedCelebrations"]

  fields = {"unlockedCelebrations." + "AMONG_US_WIN": True}
  arr = []
  for newCelebration in newUnlockedCelebrations:
    if newCelebration not in oldUnlockedCelebrations:
      fields["unlockedCelebrations." + newCelebration] = True 
      arr.append(newCelebration)

  ref = db.collection("Users").document(userId).update(fields)

  return ({"msg": arr})