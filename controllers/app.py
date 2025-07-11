from flask import Flask, render_template, request, jsonify
from models.credit import db, Credit  # Import the database and Credit model
from flask import flash, redirect, url_for
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.getenv("SECRET_KEY")


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
        interest_rate=float(data['interest_rate']),
        term=data['term'],
        grant_day=data['grant_day']
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
    credit.client = request.form['client']
    credit.amount = request.form['amount']
    credit.interest_rate = request.form['interest_rate']
    credit.term = request.form['term']
    credit.grant_day = request.form['grant_day']
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