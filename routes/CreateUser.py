from flask import Blueprint, request, jsonify
from database.database import db
from firebase_admin import exceptions
import datetime
from datetime import date
import uuid
from flask_cors import CORS, cross_origin


createUser = Blueprint("createUser", __name__)
CORS(createUser)

@createUser.route("/api/user/create", methods = ["POST"])
@cross_origin(headers=['Content-Type', 'Authorization'])
def createUserRoute():
  data = request.get_json()
    
  if not data:
    return (jsonify({"msg": "Missing data"}), 400)

  userId = data.get("userId")
  fullName = data.get("fullName")
  firstName = data.get("firstName")
  lastName = data.get("lastName")
  email = data.get("email")
  imageUrl = data.get("imageUrl")

  error_log = {
    "userId": userId,
    "fullName": fullName,
    "firstName": firstName,
    "lastName": lastName,
    "email": email,
    "imageUrl": imageUrl,
  }

  for key in error_log:
    if not error_log.get(key):
      return (jsonify({"error": "Missing {}".format(key)}), 400)

  docs = db.collection('Users')
  result = docs.where("userId", "==", userId).stream()

  for doc in result:
    return ({"msg": "User already exists"})

  # IF SOMEONE ELSE HAS SAME ID, IT OVERRIDES
  data["completedTodos"] = 0
  data["failedTodos"] = 0
  data["friendCount"] = 0
  data["selectedBadge"] = "NORMIE"
  data["selectedBorder"] = "BLACK"
  data["selectedCelebration"] = "AMONG_US_WIN"
  data["unlockedBadges"] = {"NORMIE": True}
  data["unlockedBorders"] = {"BLACK": True}
  data["unlockedCelebrations"] = {"AMONG_US_WIN": True}
  db.collection("Users").document(userId).set(data)

  dueDate = "2025-10-10T10:00:08.920Z"
  dueDate = datetime.datetime.strptime(dueDate, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp() * 1000

  addedDate = date.today()
  addedDate.strftime('%y-%m-%d')
  addedDate = str(addedDate)

  todoId = str(uuid.uuid4())

  db.collection("Todo").document(todoId).set({
    "todoName": "Easiest Todo of Your Life!",
    "dueDate": dueDate,
    "imageUrl": "https://i.imgur.com/lTTxLGM.jpg",
    "description": "Hey There! Welcome to TasksAmongUs, a great way to for you and your friends to keep each other accountable for your goals. Go to your profile page to click \"finish\" on this todo!",
    "addedDate": addedDate,
    "todoId": todoId,
    "status": False,
    "userId": userId,
    "completedDate": dueDate + 1
  })

  return ({"msg": "User created"})