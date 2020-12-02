from flask import request, Blueprint

getTodoByUser = Blueprint("getTodoByUser", __name__)

@getTodoByUser.route("/api/user/<id>/todo", methods=["GET"])
def getTodoByUserRoute(id):
  
  return {"todo" : ["todo1", "todo2", "todo3"]}