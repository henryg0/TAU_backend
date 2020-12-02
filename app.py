from flask import Flask, Blueprint
from .routes.HelloWorld import helloWorld
from .routes.GetAllTodoByUser import getAllTodoByUser
from .routes.GetTodoByFriend import getTodoByFriend
from .routes.CreateTodo import createTodo
from .routes.UpdateTodo import updateTodo
from .routes.DeleteTodo import deleteTodo
from .routes.CreateUser import createUser
from .routes.GetUser import getUser
from .routes.CreateFriendRequest import createFriendRequest
from .routes.GetFriendRequest import getFriendRequest
from .routes.GetPendingFriendRequest import getPendingFriendRequest
from .routes.DeleteFriendRequest import deleteFriendRequest
from .routes.DeleteFriend import deleteFriend
from .routes.AcceptFriendRequest import acceptFriendRequest
from .routes.GetAllFriends import getAllFriends
from .routes.GetTodo import getTodo
from .routes.SearchUser import searchUser
from .routes.GetFinishedTodo import getFinishedTodo
from .routes.GetUpcomingTodo import getUpcomingTodo
from .routes.GetWeeklyProgress import getWeeklyProgress
from .routes.FinishTodo import finishTodo
from .routes.UpdateSelectedBadge import updateSelectedBadge
from .routes.UpdateSelectedBorder import updateSelectedBorder
from .routes.UpdateSelectedCelebration import updateSelectedCelebration
from .routes.UpdateUnlockedBadges import updateUnlockedBadges
from .routes.UpdateUnlockedBorders import updateUnlockedBorders
from .routes.UpdateUnlockedCelebrations import updateUnlockedCelebrations

app = Flask(__name__)

app.register_blueprint(helloWorld)
app.register_blueprint(getAllTodoByUser)
app.register_blueprint(getTodoByFriend)
app.register_blueprint(createTodo)
app.register_blueprint(updateTodo)
app.register_blueprint(deleteTodo)
app.register_blueprint(createUser)
app.register_blueprint(getUser)
app.register_blueprint(createFriendRequest)
app.register_blueprint(getFriendRequest)
app.register_blueprint(getPendingFriendRequest)
app.register_blueprint(deleteFriendRequest)
app.register_blueprint(deleteFriend)
app.register_blueprint(acceptFriendRequest)
app.register_blueprint(getAllFriends)
app.register_blueprint(getTodo)
app.register_blueprint(searchUser)
app.register_blueprint(getFinishedTodo)
app.register_blueprint(getUpcomingTodo)
app.register_blueprint(getWeeklyProgress)
app.register_blueprint(finishTodo)
app.register_blueprint(updateSelectedBadge)
app.register_blueprint(updateSelectedBorder)
app.register_blueprint(updateSelectedCelebration)
app.register_blueprint(updateUnlockedBadges)
app.register_blueprint(updateUnlockedBorders)
app.register_blueprint(updateUnlockedCelebrations)

@app.route('/')
def hello_world():
  return 'Hello, World!'

if __name__ == "__main__":
  app.run(debug=True)

