from flask import Flask, request
from flask_socketio import join_room, leave_room, send, SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import psycopg2

import os

# Flask app setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "sekret"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc@localhost:5432/example'

db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    socketio.run(app, host="0.0.0.0", port=8080, debug=True, allow_unsafe_werkzeug=True)
