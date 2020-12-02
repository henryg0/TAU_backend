from flask import request, Blueprint, jsonify
from ..database.database import db
from firebase_admin import firestore
import datetime
import time
from flask_cors import CORS, cross_origin


getAllTodoByUser = Blueprint("getAllTodoByUser", __name__)
CORS(getAllTodoByUser)

@getAllTodoByUser.route("/api/user/<userId>/todo", methods=["GET"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def getAllTodoByUserRoute(userId):
  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)
  
  docs = db.collection('Todo').where("userId", "==", userId).order_by(u'dueDate', direction=firestore.Query.ASCENDING).stream()
  # results = docs.where("userId", "==", userId).order_by('dueDate').limit(3).stream()
  
  # res = [doc.to_dict() for doc in result]

  # print(res)
  
  sorted_results = [doc.to_dict() for doc in docs if doc.to_dict()["dueDate"] <= doc.to_dict().get("completedDate") and not doc.to_dict().get("status") and doc.to_dict()["dueDate"] > time.time() * 1000] 
  
  return {"todos": sorted_results}