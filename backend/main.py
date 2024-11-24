from flask import Flask
from flask_socketio import join_room, leave_room, send, SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import datetime

# Flask app setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "sekret"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:abc@localhost:5432/example"

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

db = SQLAlchemy(app)


# Models
class Majors(db.Model):
    __tablename__ = "majors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    major = db.Column(db.String())

    users = db.relationship("Users", back_populates="major")


class StudyLocations(db.Model):
    __tablename__ = "study_locations"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(), nullable=False)

    users = db.relationship("Users", back_populates="study_location")


class StudyTypes(db.Model):
    __tablename__ = "study_types"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    study_type = db.Column(db.String(), nullable=False)

    users = db.relationship("Users", back_populates="study_type")


class LearningStyles(db.Model):
    __tablename__ = "learning_styles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    learning_style = db.Column(db.String(), nullable=False)

    users = db.relationship("Users", back_populates="learning_style")


class BuddySuggestionsUsers(db.Model):
    __tablename__ = "buddy_suggestions_users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    suggester_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    suggested_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)


class Buddies(db.Model):
    __tablename__ = "buddies"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    accepted = db.Column(db.Boolean, nullable=False, default=False)

    user = db.relationship("Users", back_populates="buddies")


class UsersCourses(db.Model):
    __tablename__ = "users_courses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)

    user = db.relationship("Users", back_populates="courses")
    course = db.relationship("Courses", back_populates="users")


class Courses(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String, nullable=False)

    users = db.relationship("UsersCourses", back_populates="course", cascade="all, delete-orphan")
    notes = db.relationship("Notes", back_populates="course", cascade="all, delete-orphan")


class Notes(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)

    course = db.relationship("Courses", back_populates="notes")


class StudySessions(db.Model):
    __tablename__ = "study_sessions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_type = db.Column(db.String, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey("chats.id", ondelete="CASCADE"), nullable=False)

    users = db.relationship("Users", secondary="users_study_sessions", back_populates="study_sessions")
    chat = db.relationship("Chats", back_populates="study_sessions")


class UserStudySessions(db.Model):
    __tablename__ = "users_study_sessions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    study_session_id = db.Column(db.Integer, db.ForeignKey("study_sessions.id", ondelete="CASCADE"), nullable=False)


class Chats(db.Model):
    __tablename__ = "chats"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chat_name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    study_sessions = db.relationship("StudySessions", back_populates="chat", cascade="all, delete-orphan")
    messages = db.relationship("Messages", secondary="chat_messages", back_populates="chats")


class Messages(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    chats = db.relationship("Chats", secondary="chat_messages", back_populates="messages")


class ChatMessages(db.Model):
    __tablename__ = "chat_messages"
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey("chats.id", ondelete="CASCADE"), nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey("messages.id", ondelete="CASCADE"), nullable=False)


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    autobiography = db.Column(db.Text, nullable=True)
    major_id = db.Column(db.Integer, db.ForeignKey("majors.id"))
    year = db.Column(db.Integer, nullable=False)
    availability = db.Column(db.String(), nullable=False)
    study_location_id = db.Column(db.Integer, db.ForeignKey("study_locations.id"))
    study_type_id = db.Column(db.Integer, db.ForeignKey("study_types.id"))
    learning_style_id = db.Column(db.Integer, db.ForeignKey("learning_styles.id"))

    major = db.relationship("Majors", back_populates="users")
    study_location = db.relationship("StudyLocations", back_populates="users")
    study_type = db.relationship("StudyTypes", back_populates="users")
    learning_style = db.relationship("LearningStyles", back_populates="users")
    buddies = db.relationship("Buddies", back_populates="user", cascade="all, delete-orphan")
    courses = db.relationship("UsersCourses", back_populates="user", cascade="all, delete-orphan")
    study_sessions = db.relationship("StudySessions", secondary="users_study_sessions", back_populates="users")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    socketio.run(app, host="0.0.0.0", port=8080, debug=True)