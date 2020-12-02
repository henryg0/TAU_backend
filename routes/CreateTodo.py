from flask import Blueprint, request, jsonify
from database.database import db
import uuid
import datetime
from datetime import date
import time
from flask_cors import CORS, cross_origin


createTodo = Blueprint("createTodo", __name__)
CORS(createTodo)

@createTodo.route("/api/user/<userId>/todo/create", methods=["POST"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def createTodoRoute(userId):
  if not userId:
    return (jsonify({"error": "Missing userId"}), 400)    

  data = request.get_json()

  if not data:
    return (jsonify({"msg": "Missing data"}), 400)

  todoName = data.get("todoName")
  description = data.get("description")
  imageUrl = data.get("imageUrl")
  dueDate = data.get("dueDate")
  
  # 2020-10-21T10:00:08.920Z
  dueDate = int(dueDate)
  # dueDate = datetime.datetime.strptime(dueDate, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp() * 1000
  
  error_log = {
    "todoName":todoName,
    "dueDate":dueDate,
    "imageUrl":imageUrl,
  }
  
  for key in error_log:
    if not error_log[key]:
      return (jsonify({"error": "Missing {}".format(key)}), 400)

  # do the converting
  addedDate = date.today()
  addedDate.strftime('%y-%m-%d')
  
  todoId = str(uuid.uuid4())
  status = False

  data["addedDate"] = str(addedDate)
  data["todoId"] = todoId
  data["status"] = status
  data["userId"] = userId
  data["dueDate"] = dueDate
  data["completedDate"] = dueDate + 1
  
  db.collection("Todo").document(todoId).set(data)
  return data