from flask import request, Blueprint, jsonify
from database.database import db
from firebase_admin import firestore
import datetime
import time
from flask_cors import CORS, cross_origin


getFinishedTodo = Blueprint("getFinishedTodo", __name__)
CORS(getFinishedTodo)

@getFinishedTodo.route("/api/user/<userId>/todo/finish", methods=["GET"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def getFinishedTodoRoute(userId):
  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)
  
  friends = db.collection("Friends").where("userId", "==", userId).stream()

  idDict = {doc.to_dict()["friendId"]:True for doc in friends}
  idDict[userId] = True

  currentTime = time.time() * 1000

  docs = db.collection('Todo').where('completedDate', '<', currentTime).order_by(u'completedDate', direction=firestore.Query.DESCENDING).stream()
  
  sortedResults = [doc.to_dict() for doc in docs] #if idDict[doc.to_dict("userId")]]
  
  res = []

  users = db.collection('Users').stream()
  user_dicts = [user.to_dict() for user in users]

  for todo in sortedResults:
    if idDict.get(todo["userId"]):
      for user in user_dicts:
        if todo["userId"] == user["userId"]:
          todo["selectedBadge"] = user["selectedBadge"]
          todo["selectedBorder"] = user["selectedBorder"]
          todo["selectedCelebration"] = user["selectedCelebration"]
          todo["profileUrl"] = user["imageUrl"]
          todo["fullName"] = user["fullName"]
      res.append(todo)

  return {"todos": res}