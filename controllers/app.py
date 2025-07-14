from flask import Flask, render_template, request, jsonify
from models.credit import db, Credit  # Import the database and Credit model
from flask import flash, redirect, url_for
from dotenv import load_dotenv
from datetime import datetime
from collections import defaultdict
from datetime import datetime
import os

# Load environment variables from .env file
load_dotenv()  
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.getenv("SECRET_KEY")


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///credits.db'  # Database URI for SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy extension with the Flask app
db.init_app(app)  

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

    #Obtain the count of credits
    credits = Credit.query.all()
    # Count the number of credits
    total_credits = len(credits)  
    # Calculate the total amount of all credits
    total_amount = sum(credit.amount for credit in credits)  
    # Get the last 3 credits for display
    last_credits = Credit.query.order_by(Credit.grant_day.desc()).limit(3).all()
    return render_template('index.html', total_credits=total_credits, total_amount=total_amount, last_credits=last_credits)  # Render the main page


#################### API routes to get credit data for charts
# Get credit data by client for chart
@app.route('/api/credit_by_client')
def credit_by_client():
    # Query all credits and group by client
    credits = Credit.query.all()
    client_totals = {}
    # Sum amounts for each client
    for credit in credits:
        client_totals[credit.client] = client_totals.get(credit.client, 0) + credit.amount
    # Prepare data for the chart
    data = {
        "labels": list(client_totals.keys()),
        "amounts": list(client_totals.values())
    }
    # Return the data as JSON
    return jsonify(data)

# Get total credit amount by month for chart
@app.route('/api/total_credit')
def total_credit():
    credits = Credit.query.all()

    # Group by month
    monthly_totals = defaultdict(float)

    for credit in credits:
        if credit.grant_day:  # Ensure grant_day is not None
            # Parse the date and extract the month
            date_obj = datetime.strptime(credit.grant_day, '%Y-%m-%d')
            month_label = date_obj.strftime('%b')  
            monthly_totals[month_label] += credit.amount

    # Order according month
    ordered_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    labels = []
    amounts = []
    # Prepare the data for the chart by matching the ordered months with the calculated monthly totals
    for month in ordered_months:
        if month in monthly_totals:
            labels.append(month)
            amounts.append(monthly_totals[month])
    # Prepare the final data structure for the chart
    data = {
        "labels": labels,
        "amounts": amounts
    }
    # Return the data as JSON
    return jsonify(data)

# Get credit data by amount range for chart
@app.route('/api/credit_by_range')
def credit_by_range():
    credits = Credit.query.all()
    # Initialize ranges for credit amounts
    ranges = {
        "0 - 5000": 0,
        "5001 - 20000": 0,
        "20001+": 0
    }

    # Count credits in each range
    for credit in credits:
        if credit.amount <= 5000:
            ranges["0 - 5000"] += 1
        elif credit.amount <= 20000:
            ranges["5001 - 20000"] += 1
        else:
            ranges["20001+"] += 1

    # Prepare the data for the chart
    data = {
        "labels": list(ranges.keys()),
        "amounts": list(ranges.values())
    }
    # Return the data as JSON
    return jsonify(data)

   
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
    credits = Credit.query.order_by(Credit.id.desc()).all()
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