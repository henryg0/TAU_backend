from database import session

session.execute("LIST ROLES")
session.execute("SELECT * FROM system_schema.keyspaces")

session.execute("USE todo")

session.execute("DROP TABLE IF EXISTS todo.UserProfile")
query = "CREATE TABLE IF NOT EXISTS todo.UserProfile( {}, {}, {}, {}, {} )".format(
  "userId varint PRIMARY KEY", 
  "firstName text", 
  "lastName text", 
  "email text",
  "imageUrl text"
)
session.execute(query)
session.execute("DROP TABLE IF EXISTS todo.UserTodo")
query = "CREATE TABLE IF NOT EXISTS todo.UserTodo( {}, {}, {}, {}, {}, {}, {}, {}, {} ) WITH CLUSTERING ORDER BY (duedate ASC)".format(
  "userId varint",
  "todoId uuid",
  "status boolean",
  "addedDate text",
  "duedate timestamp",
  "todoName text",
  "description text",
  "imageUrl text",
  "PRIMARY KEY (userId, duedate)"
)

session.execute(query)
session.execute("DROP TABLE IF EXISTS todo.UserFriends")
query = "CREATE TABLE IF NOT EXISTS todo.UserFriends( {}, {}, {}, {}, {} )".format(
  "userId varint PRIMARY KEY", 
  "friendId varint",
  "firstName text", 
  "lastName text",
  "status text"
)

session.execute(query)
