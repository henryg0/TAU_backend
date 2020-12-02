import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv

load_dotenv(".env")

cred = credentials.Certificate('./database/firebase-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# from cassandra.cluster import Cluster
# from cassandra.auth import PlainTextAuthProvider
# import os
# from dotenv import load_dotenv

# cloud_config= {
#   'secure_connect_bundle': './database/secure-connect-tasks-among-us.zip'
# }

# # load_dotenv("../.env")
# load_dotenv(".env")

# auth_provider = PlainTextAuthProvider(os.environ.get("database_username"), os.environ.get("database_password"))
# cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
# session = cluster.connect('todo')

# if __name__ == "__main__":
#   row = session.execute("select release_version from system.local").one()
#   if row:
#     print(row[0])
#   else:
#     print("An error occurred.")

#   print ("hi")