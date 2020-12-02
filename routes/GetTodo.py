from flask import Blueprint, request, jsonify
from database.database import db
from flask_cors import CORS, cross_origin


getTodo = Blueprint("getTodo", __name__)
CORS(getTodo)

@getTodo.route("/api/todo/<todoId>", methods=["GET"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def getTodoRoute(todoId):
  if not todoId:
    return (jsonify({"error": "Missing todoId"}), 400)    

  doc = db.collection("Todo").document(todoId).get()

  if not doc.exists:
    return (jsonify({"error": "Todo doesn't exist"}), 400)  

  doc = doc.to_dict()
  
  return {"todo": doc}