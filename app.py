from flask import Flask, render_template, request
import pickle
import numpy as np
from db import Database
import os

app = Flask(__name__)
db = Database()

with open('Research/loan_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('front.html')

@app.route('/home', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        gender = request.form['Gender']
        married = request.form['Married']
        dependents = request.form['Dependents']
        education = request.form['Education']
        self_employed = request.form['Self_Employed']
        loan_amount = float(request.form['LoanAmount'])
        loan_amount_term = int(request.form['Loan_Amount_Term'])
        credit_history = int(request.form['Credit_History'])
        property_area = request.form['Property_Area']
        family_income = float(request.form['family_income'])
        pred = model.predict([[gender, married, dependents, education, self_employed, loan_amount, loan_amount_term, credit_history, property_area, family_income]])[0]

        db.save_prediction(gender, married, dependents, education, self_employed, loan_amount, loan_amount_term, credit_history, property_area, family_income, pred)
        
        if pred == 'Y':
            pred = "Loan Approved "
        else:
            pred = "Loan Rejected "
        return render_template('home.html', prediction_text=pred)

    return render_template('home.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
