from flask import request, Blueprint, jsonify
from database.database import db
from firebase_admin import firestore
import datetime
import time
from flask_cors import CORS, cross_origin


getUpcomingTodo = Blueprint("getUpcomingTodo", __name__)
CORS(createUser)


@getUpcomingTodo.route("/api/user/<userId>/todo/upcoming", methods=["GET"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def getUpcomingTodoRoute(userId):
  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)
  
  friends = db.collection("Friends").where("userId", "==", userId).stream()

  idDict = {doc.to_dict()["friendId"]:True for doc in friends}
  idDict[userId] = True

  currentTime = time.time() * 1000

  docs = db.collection('Todo').where('dueDate', '>=', currentTime).order_by(u'dueDate', direction=firestore.Query.ASCENDING).stream()
  
  sortedResults = [doc.to_dict() for doc in docs]
  
  res = []
  
  users = db.collection('Users').stream()
  user_dicts = [user.to_dict() for user in users]

  for todo in sortedResults:
    if idDict.get(todo["userId"]) and not todo.get("status"):
      for user in user_dicts:
        if todo["userId"] == user["userId"]:
          todo["selectedBadge"] = user["selectedBadge"]
          todo["selectedBorder"] = user["selectedBorder"]
          todo["selectedCelebration"] = user["selectedCelebration"]
          todo["profileUrl"] = user["imageUrl"]
          todo["fullName"] = user["fullName"]
      res.append(todo)
  
  # custom items, full name, and imageUrl
  return {"todos": res}