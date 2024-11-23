from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql  # Import pymysql to replace MySQLdb

# Install pymysql as MySQLdb
pymysql.install_as_MySQLdb()

# Initialize Flask app
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing) for frontend-backend communication
CORS(app)

# Configure SQLAlchemy for database connection
# Use pymysql in the connection URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/studybuddy_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a simple route for testing
@app.route('/')
def home():
    return jsonify({'message': 'Hello, World!'})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
