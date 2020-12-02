from flask import request, Blueprint

helloWorld = Blueprint("helloWorld", __name__)

@helloWorld.route("/api/helloWorld", methods=["POST"])
def helloWorldRoute():
  return 'Hello World!'

