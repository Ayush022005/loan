# EduFin: Education Loan Repayment Prediction System

EduFin is a predictive system designed to determine whether an individual is eligible to repay an education loan. If the prediction suggests that the person may not be able to repay the loan, they will not qualify for the loan.

## Project Overview

This project consists of a Flask web application that takes input parameters from users and utilizes a machine learning model to predict the likelihood of loan repayment based on various factors such as age, purpose of the loan, CIBIL score, current debts, duration, current assets, and monthly income.

## How to Use

1. **Clone the Repository:**
   ```
   git clone https://github.com/Ayush022005/loan.git
   ```

2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```
   python app.py
   ```

4. **Access the Application:**
   Visit `http://localhost:5000` in your web browser.

## Code Structure

- **app.py**: Contains the Flask application code including routes and loan approval algorithm.
- **templates/index.html**: HTML template for the user interface to input loan application details.
- **templates/confirmation.html**: HTML template for displaying the loan approval result.

## Requirements

- Python 3.x
- Flask
- scikit-learn
- pickle

## Usage

- Users can input their details including name, age, purpose of the loan, loan amount, CIBIL score, current debts, loan duration, current assets, and monthly income.
- The system then evaluates the input against predefined criteria and provides a loan approval result.


## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify and expand the README.md according to your project's specific requirements and details!
