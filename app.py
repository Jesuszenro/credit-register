from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///credits.db'  # Database URI for SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True)    # Unique identifier for each credit
    client = db.Column(db.String(80), nullable=False)   # Client's name 
    amount = db.Column(db.Float, nullable=False)    # Amount of credit in currency units
    interest_rate = db.Column (db.Float, nullable=False)    # Annual interest rate in percentage
    term = db.Column(db.Integer, nullable=False)  # Term in months
    grant_day = db.Column (db.String(10), nullable=False)   # Start date of the credit in YYYY-MM-DD format

with app.app_context():
    db.create_all()  # Create the database tables if they don't exist