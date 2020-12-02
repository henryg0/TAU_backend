from flask import Blueprint

getTodoByFriend = Blueprint("getTodoByFriend", __name__)

@getTodoByFriend.route("/api/friend/<id>", methods=["GET"])
def getTodoByFriendRoute(id):
  return { "todo" : ["todo1", "todo2", "todo3"]}
