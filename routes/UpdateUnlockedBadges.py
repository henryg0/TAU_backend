from flask import Blueprint, request, jsonify
from database.database import db
from firebase_admin import exceptions, firestore
from flask_cors import CORS, cross_origin


updateUnlockedBadges = Blueprint("updateUnlockedBadge", __name__)
CORS(updateUnlockedBadge)

@updateUnlockedBadges.route("/api/user/<userId>/unlocked/badges/update", methods = ["PUT"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def updateUnlockedBadgesRoute(userId):
  data = request.get_json()

  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)

  if not data:
    return (jsonify({"msg": "Missing data"}), 400)

  newUnlockedBadges = data.get("unlockedBadges")
  user = db.collection('Users').where("userId", "==", userId).stream()
  oldUnlockedBadges = [doc.to_dict() for doc in user][0]["unlockedBadges"]

  fields = {"unlockedBadges.NORMIE": True}
  arr = []
  for newBadge in newUnlockedBadges:
    if newBadge not in oldUnlockedBadges:
      fields["unlockedBadges." + newBadge] = True 
      arr.append(newBadge)

  ref = db.collection("Users").document(userId).update(fields)

  return ({"msg": arr})