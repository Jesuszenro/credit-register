from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Credit(db.Model):
    id = db.Column(db.Integer, primary_key=True)    # Unique identifier for each credit
    client = db.Column(db.String(80), nullable=False)   # Client's name 
    amount = db.Column(db.Float, nullable=False)    # Amount of credit in currency units
    interest_rate = db.Column (db.Float, nullable=False)    # Annual interest rate in percentage
    term = db.Column(db.Integer, nullable=False)  # Term in months
    grant_day = db.Column (db.String(10), nullable=False)   # Start date of the credit in YYYY-MM-DD format