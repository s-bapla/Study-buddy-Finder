from flask import Flask, request
from flask_socketio import join_room, leave_room, send, SocketIO

from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from utils.db import get_db_connection_url

# Flask app setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "sekret"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Configure SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = get_db_connection_url()
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = "Users"


@app.before_first_request
def initialize_database():
    """Create tables if they don't exist."""
    db.create_all()


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8080, debug=True, allow_unsafe_werkzeug=True)
