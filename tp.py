from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib

# Read the dataset
loans = pd.read_csv('./loans.csv')

# Encode the 'purpose' column
label_encoder = LabelEncoder()
loans['purpose_encoded'] = label_encoder.fit_transform(loans['purpose'])

# Define features and target variable
X = loans[['credit.policy', 'int.rate', 'installment', 'log.annual.inc', 'dti', 'fico', 'days.with.credit.line', 'revol.bal', 'revol.util', 'inq.last.6mths', 'delinq.2yrs', 'public.rec', 'purpose_encoded']]
y = loans['not.fully.paid']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_classifier.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Export the trained Random Forest model to a file (e.g., 'random_forest_model.pkl')
rf_model_filename = 'random_forest_model.pkl'
joblib.dump(rf_classifier, rf_model_filename)
print(f'Trained Random Forest model has been exported to {rf_model_filename}')
