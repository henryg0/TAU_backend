from flask import Blueprint, request, jsonify
from database.database import db
from firebase_admin import exceptions
from flask_cors import CORS, cross_origin


updateSelectedBorder = Blueprint("updateSelectedBorder", __name__)
CORS(updateSelectedBorder)

@updateSelectedBorder.route("/api/user/<userId>/selected/border/update", methods = ["PUT"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def updateSelectedBadgeRoute(userId):
  data = request.get_json()

  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)

  if not data:
    return (jsonify({"msg": "Missing data"}), 400)

  selectedBorder = data.get("selectedBorder")

  error_log = {
    "selectedBorder": selectedBorder,
  }

  for key in error_log:
    if not error_log.get(key):
      return (jsonify({"error": "Missing {}".format(key)}), 400)

  db.collection("Users").document(userId).update({"selectedBorder": selectedBorder})

  return ({"msg": "Selected Border Updated"})