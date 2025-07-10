from flask import Flask, render_template, request, jsonify
from models.credit import db, Credit  # Import the database and Credit model


app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///credits.db'  # Database URI for SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Initialize the SQLAlchemy extension with the Flask app

with app.app_context():
    db.create_all()  # Create the database tables if they don't exist


@app.route('/')
def index():
    return render_template('index.html')  # Render the main page

################# CRUD operations for credits 
# Register a new credit
@app.route('/credits', methods=['POST'])    
def register_credit():
    data = request.form   # Get JSON data from the request
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

@app.route('/credits/new', methods=['GET'])
def new_credit():
    return render_template('new_credit.html')

# Get all credits
@app.route('/credits/view', methods=['GET'])
def view_credits():
    credits = Credit.query.all()
    return render_template('credits.html', credits=credits)

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