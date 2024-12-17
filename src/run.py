from main.server.server import app
from models.settings.db_connection_handle import db_connection_handler

if __name__ == "__main__":
  db_connection_handler.connect()
  app.run(host="0.0.0.0", port=3000, debug=True)