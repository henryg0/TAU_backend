from flask import request, Blueprint, jsonify
from database.database import db
from firebase_admin import firestore
import datetime
import time
from flask_cors import CORS, cross_origin


getWeeklyProgress = Blueprint("getWeeklyProgress", __name__)
CORS(getWeeklyProgress)

@getWeeklyProgress.route("/api/user/<userId>/weekly", methods=["GET"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def getWeeklyProgressRoute(userId):
  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)
  
  # each week: 604800000
  lowerBound = int(time.time()*1000) - 604800000
  
  # each day: 86400000 ms
  currentTime = int(time.time()*1000)

  docs = db.collection("Todo").where("userId", "==", userId).order_by("completedDate", direction=firestore.Query.ASCENDING).start_at({u'completedDate' : lowerBound}).end_at({u'completedDate' : currentTime}).stream()
  docDict = [doc.to_dict() for doc in docs]
  
  todoDates = {datetime.datetime.fromtimestamp(todo["completedDate"]/1000).strftime("%m/%d/%Y") : [[], []] for todo in docDict}
    
  
  for todo in docDict:
    # weekday = datetime.datetime(todo["completedDate"]).get_weekday()
    day = datetime.datetime.fromtimestamp(todo["completedDate"]/1000).strftime("%m/%d/%Y")

    # day = weekdays[weekday]
    if todo.get("status"):
      todoDates[day][0].append(todo)
    else:
      if currentTime > todo["completedDate"]:
        todoDates[day][1].append(todo)
  
  completed = [{"name": int(datetime.datetime.strptime(dateCompleted, "%m/%d/%Y").timestamp()), "completed":len(todoDates[dateCompleted][0]), "failed":len(todoDates[dateCompleted][1])} for dateCompleted in todoDates]
  completed = [{"completed":0, "failed":0}]*(7-len(completed)) + completed
  return {"todos": completed}