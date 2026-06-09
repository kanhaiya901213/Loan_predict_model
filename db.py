import os
import pymysql as sql

class Database:
    
    def __init__(self):
        self.conn = sql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = '901213',
            database = 'loan_prediction_db'
        )
        self.cursor = self.conn.cursor()
        print("Database connection established.")

        # step2 : create table
        self.cursor.execute('''create table if not exists loan_data(
            Gender varchar(10),
            Married varchar(10),
            Dependents varchar(10),
            Education varchar(20),
            Self_Employed varchar(10),
            LoanAmount float,
            Loan_Amount_Term int,
            Credit_History int,
            Property_Area varchar(20),
            family_income float,
            prediction varchar(10))''')
    
    def save_prediction(self, Gender, Married, Dependents, Education, Self_Employed, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, family_income, prediction):
        query = '''insert into loan_data(Gender, Married, Dependents, Education, Self_Employed, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, family_income, prediction) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        self.cursor.execute(query, (Gender, Married, Dependents, Education, Self_Employed, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, family_income, prediction))
        self.conn.commit()
        print("Prediction saved to database.")
obj = Database()