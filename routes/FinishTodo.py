from flask import request, Blueprint, jsonify
from database.database import db
from firebase_admin import firestore
from google.cloud.firestore_v1 import Increment
import time
from flask_cors import CORS, cross_origin


finishTodo = Blueprint("finishTodo", __name__)
CORS(finishTodo)


@finishTodo.route("/api/user/<userId>/todo/<todoId>/status/complete", methods=["PATCH"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def finishTodoRoute(userId, todoId):
  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)
    
  if not todoId:
    return (jsonify({"error": "Missing todoId"}), 400)    
  
  doc = db.collection("Todo").document(todoId).get()
  
  if not doc.exists:
    return (jsonify({"error": "Todo does not exist"}), 404)

  docDict = doc.to_dict()

  if not (docDict.get("userId") and docDict["userId"] == userId):
    return (jsonify({"error": "User is not allowed to update this field"}), 403)

  currentTime = int(time.time() * 1000)
  
  if docDict["dueDate"] < currentTime:
    return {"msg": "You have failed to complete the assignment in time :("}
  
  elif not docDict.get("status"):
    docDict["status"] = True
    docDict["completedDate"] = currentTime
    db.collection("Users").document(userId).update({'finishedTodos': Increment(1)})
  
  db.collection("Todo").document(todoId).set(docDict)
  
  return {"todo": docDict}