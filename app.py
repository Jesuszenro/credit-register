from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the main page

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

# CRUD operations for credits 

    # Register a new credit
@app.route('/credits', methods=['POST'])    
def register_credit():
    data = request.get_json()   # Get JSON data from the request
    new_credit = Credit(
        client=data['client'],
        amount=data['amount'],
        interest_rate=data['interest_rate'],
        term=data['term'],
        grant_day=data['grant_day']
    )
    db.session.add(new_credit)
    db.session.commit()
    return jsonify({'message': 'Credit registered successfully!'}), 201

# Get all credits
@app.route('/credits', methods=['GET'])
def get_credits():
    credits = Credit.query.all()    # Query all credits from the database
    output = []
    for credit in credits:
        output.append({
            'id': credit.id,    
            'client': credit.client,    
            'amount': credit.amount,
            'interest_rate': credit.interest_rate,    
            'term': credit.term,    
            'grant_day': credit.grant_day    
        })
    return jsonify(output), 200

# Update a credit
@app.route('/credits/<int:id>', methods=['PUT'])    # Route to edit a credit by its ID
def update_credit (id):
    credit = Credit.query.get_or_404(id)    # Get the credit by ID or return 404 if not found
    data = request.get_json()    # Get JSON data from the request
    # Update the credit fields with the provided data, if available
    credit.client = data.get('client', credit.client)   
    credit.amount = data.get('amount', credit.amount)    
    credit.interest_rate = data.get('interest_rate', credit.interest_rate)    
    credit.term = data.get('term', credit.term)    
    credit.grant_day = data.get('grant_day', credit.grant_day)    
    db.session.commit()    
    return jsonify({'message': 'Credit updated successfully!'}), 200

# Delete a credit
@app.route('/credits/<int:id>', methods=['DELETE'])    # Route to delete a credit by its ID
def delete_credit(id):
    credit = Credit.query.get_or_404(id)    
    db.session.delete(credit)    # Delete the credit from the database
    db.session.commit()
    return jsonify({'message': 'Credit deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)    # Run the Flask application in debug mode