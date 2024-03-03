from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        purpose = request.form['purpose']
        amount = request.form['amount']
        cibil_score = request.form['cibil_score']
        current_debts = request.form['current_debts']
        duration = request.form['duration']
        current_assets = request.form['current_assets']
        monthly_income = request.form['monthly_income']

        # Call the loan approval algorithm
        result = loan_approval_algorithm(name, age, purpose, amount, cibil_score, current_debts, duration, current_assets, monthly_income)

        return render_template('confirmation.html', result=result)

    return render_template('index.html')

def loan_model():
    
# Specify the path to your Pickle file
    model_file_path = './model.pkl'

# Load the Pickle model
    with open(model_file_path, 'rb') as file:
        loaded_model = pickle.load(file)

    return loaded_model

def loan_approval_algorithm(name, age, purpose, amount, cibil_score, current_debts, duration, current_assets, monthly_income):
    # Convert input values to appropriate data types
    try:
        age = int(age)
        cibil_score = int(cibil_score)
        monthly_income = float(monthly_income)
    except ValueError:
        return {
            'error': 'Invalid age, CIBIL score, or monthly income. Please enter valid numbers.',
            'name': name,
            'age': age,
            'purpose': purpose,
            'amount': amount,
            'cibil_score': cibil_score,
            'current_debts': current_debts,
            'duration': duration,
            'current_assets': current_assets,
            'monthly_income': monthly_income,
            'approval_result': ''
        }

    amount = float(amount)
    current_debts = float(current_debts)
    duration = int(duration)
    current_assets = float(current_assets)

    # Minimum requirements for loan approval
    min_cibil_score = 650
    min_duration_months = 12
    min_current_assets = 0
    min_monthly_income = 1000  # Adjust as needed

    # Additional real-life data checks
    if age < 18:
        return {
            'error': 'Applicant must be at least 18 years old.',
            'name': name,
            'age': age,
            'purpose': purpose,
            'amount': amount,
            'cibil_score': cibil_score,
            'current_debts': current_debts,
            'duration': duration,
            'current_assets': current_assets,
            'monthly_income': monthly_income,
            'approval_result': 'Applicant must be at least 18 years old.'
        }

    if cibil_score > 1000:
        return {
            'error': 'Invalid CIBIL score. Please enter a valid score up to 1000.',
            'name': name,
            'age': age,
            'purpose': purpose,
            'amount': amount,
            'cibil_score': cibil_score,
            'current_debts': current_debts,
            'duration': duration,
            'current_assets': current_assets,
            'monthly_income': monthly_income,
            'approval_result': ''
        }

    if monthly_income < min_monthly_income:
        return {
            'error': 'Monthly income should be at least $1000.',
            'name': name,
            'age': age,
            'purpose': purpose,
            'amount': amount,
            'cibil_score': cibil_score,
            'current_debts': current_debts,
            'duration': duration,
            'current_assets': current_assets,
            'monthly_income': monthly_income,
            'approval_result': ''
        }

    # Education loan specific requirements
    education_loan_amount_limit = 100000000  # Adjust as needed

    # Check eligibility based on conditions
    if purpose.lower() == "india" or purpose.lower() == "foreign":
        if cibil_score >= min_cibil_score and duration >= min_duration_months:
            if amount <= education_loan_amount_limit and current_assets >= min_current_assets:
                approval_result = f"Congratulations, {name}! Your education loan application is approved."
            else:
                approval_result = f"Sorry, {name}. Your loan amount exceeds the limit or current assets are insufficient."
        else:
            approval_result = f"Sorry, {name}. Your CIBIL score or loan duration does not meet the minimum requirements."
    else:
        approval_result = f"Sorry, {name}. Invalid loan purpose. Please choose 'India' or 'Foreign'."

    return {
        'name': name,
        'age': age,
        'purpose': purpose,
        'amount': amount,
        'cibil_score': cibil_score,
        'current_debts': current_debts,
        'duration': duration,
        'current_assets': current_assets,
        'monthly_income': monthly_income,
        'approval_result': approval_result
    }

if __name__ == '__main__':
    app.run(debug=True)
