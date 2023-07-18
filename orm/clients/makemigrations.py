from .db import DBConnection

db_connection = DBConnection()
db_connection.make_migrations()
