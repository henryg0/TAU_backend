from flask import Blueprint, request, jsonify
from database.database import db
from firebase_admin import exceptions
from flask_cors import CORS, cross_origin


updateSelectedCelebration = Blueprint("updateSelectedCelebration", __name__)
CORS(updateSelectedCelebration)

@updateSelectedCelebration.route("/api/user/<userId>/selected/celebration/update", methods = ["PUT"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def updateSelectedCelebrationRoute(userId):
  data = request.get_json()

  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)

  if not data:
    return (jsonify({"msg": "Missing data"}), 400)

  selectedCelebration = data.get("selectedCelebration")

  error_log = {
    "selectedCelebration": selectedCelebration,
  }

  for key in error_log:
    if not error_log.get(key):
      return (jsonify({"error": "Missing {}".format(key)}), 400)

  db.collection("Users").document(userId).update({"selectedCelebration": selectedCelebration})

  return ({"msg": "Selected Celebration Updated"})