from flask import Flask, render_template, request, jsonify
from models.credit import db, Credit  # Import the database and Credit model
from flask import flash, redirect, url_for
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()  # Load environment variables from .env file
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.getenv("SECRET_KEY")


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///credits.db'  # Database URI for SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Initialize the SQLAlchemy extension with the Flask app

with app.app_context():
    db.create_all()  # Create the database tables if they don't exist

# Function to validate credit data
def validate_credit_data(client, amount, interest_rate, term, grant_day):

    # Check if all fields are filled
    if not client or not amount or not interest_rate or not term or not grant_day:
        return 'All fields must be completed.'

    # Validate amount
    try:
        amount_value = float(amount)
        if amount_value <= 0:
            return 'Amount must be greater than zero.'
    except ValueError:
        return 'Amount must be a valid number.'

    # Validate interest rate
    try:
        interest_value = float(interest_rate)
        if interest_value < 0:
            return 'Interest rate cannot be negative.'
    except ValueError:
        return 'Interest rate must be a valid number.'

    # Validate term
    try:
        term_value = int(term)
        if term_value <= 0:
            return 'Term must be greater than zero.'
    except ValueError:
        return 'Term must be a valid integer.'

    # Validate grant day format
    try:
        datetime.strptime(grant_day, '%Y-%m-%d')
    except ValueError:
        return 'Grant day must be a valid date in YYYY-MM-DD format.'

    return None  # Everything OK


# Main route to render the index page
@app.route('/')
def index():
    return render_template('index.html')  # Render the main page

################# CRUD operations for credits 
# Register a new credit
@app.route('/credits', methods=['POST'])    
def register_credit():
    data = request.form   # Get data from the form request

    # Extract data from the form before creating a new credit, so we can validate it
    client = data.get('client')
    amount = data.get('amount')
    interest_rate = data.get('interest_rate')
    term = data.get('term')
    grant_day = data.get('grant_day')

    # Validate the data before creating a new credit
    error_msg = validate_credit_data(client, amount, interest_rate, term, grant_day)
    if error_msg:
        flash(error_msg, 'error')
        return redirect(url_for('new_credit'))  # Redirect back to the form if validation fails
    
    # Create a new Credit instance with the validated data
    new_credit = Credit(
        client=client,
        amount=amount,
        interest_rate=interest_rate,
        term=term,
        grant_day=grant_day
    )
    
    
    db.session.add(new_credit)
    db.session.commit()
    flash('Credit registered successfully!', 'success')  # Flash a success message
    return redirect(url_for('view_credits'))

# Render the form to add a new credit
@app.route('/credits/new', methods=['GET'])
def new_credit():
    return render_template('new_credit.html')

# Get all credits
@app.route('/credits/view', methods=['GET'])
def view_credits():
    credits = Credit.query.all()
    return render_template('credits.html', credits=credits)

# Update a credit
@app.route('/update_inline/credits/<int:id>', methods=['POST'])    # Route to edit a credit by its ID
def update_inline (id):
    credit = Credit.query.get_or_404(id)    # Get the credit by ID or return 404 if not found
    # Update the credit fields with the provided data, if available
    data = request.form

    client = data.get('client')
    amount = data.get('amount')
    interest_rate = data.get('interest_rate')
    term = data.get('term')
    grant_day = data.get('grant_day')

    # Validate the data before updating
    error_msg = validate_credit_data(client, amount, interest_rate, term, grant_day)
    if error_msg:
        flash(error_msg, 'error')
        return redirect(url_for('view_credits'))

    # Update the credit instance with the new data    
    credit.client = client
    credit.amount = float(amount)
    credit.interest_rate = float(interest_rate)
    credit.term = int(term)
    credit.grant_day = grant_day

    db.session.commit()   
    return redirect(url_for('view_credits'))    # Redirect to the view credits page

# Delete a credit
@app.route('/delete_credit/<int:id>', methods=['POST'])    # Route to delete a credit by its ID
def delete_credit(id):
    credit = Credit.query.get_or_404(id)    
    db.session.delete(credit)    # Delete the credit from the database
    db.session.commit()
    flash('Credit deleted successfully!', 'success')
    return redirect(url_for('view_credits'))
if __name__ == '__main__':
    app.run(debug=True)    # Run the Flask application in debug mode