import mysql.connector as sql
import os

class Database:
    def __init__(self):
        db_host = os.environ.get("DB_HOST", "127.0.0.1")
        db_user = os.environ.get("DB_USER", "root")         
        db_password = os.environ.get("DB_PASSWORD", "901213") 
        db_name = os.environ.get("DB_NAME", "loan_prediction_db")
        db_port = int(os.environ.get("DB_PORT", 3306))

        self.conn = sql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_name,
            port = db_port
        )
        
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS loan_data (
            Gender VARCHAR(20),
            Married VARCHAR(20),
            Dependents VARCHAR(10),
            Education VARCHAR(50),
            Self_Employed VARCHAR(20),
            LoanAmount FLOAT,
            Loan_Amount_Term INT,
            Credit_History INT,
            Property_Area VARCHAR(50),
            family_income FLOAT,
            Prediction VARCHAR(50)
        )''')
        # self.cursor.close()


# class Database:
#     def __init__(self):
#         self.conn = sql.connect(
#             host = '127.0.0.1',
#             port = 3306,
#             user = 'root',
#             password = '901213',
#             database = 'loan_prediction_db'
#         )
#         self.cursor = self.conn.cursor()
#         print("Database connection established.")

#         # step2 : create table
#         self.cursor.execute('''create table if not exists loan_data(
#             Gender varchar(10),
#             Married varchar(10),
#             Dependents varchar(10),
#             Education varchar(20),
#             Self_Employed varchar(10),
#             LoanAmount float,
#             Loan_Amount_Term int,
#             Credit_History int,
#             Property_Area varchar(20),
#             family_income float,
#             prediction varchar(10))''')
    
    def save_prediction(self, Gender, Married, Dependents, Education, Self_Employed, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, family_income, prediction):
        query = '''insert into loan_data(Gender, Married, Dependents, Education, Self_Employed, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, family_income, prediction) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        self.cursor.execute(query, (Gender, Married, Dependents, Education, Self_Employed, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, family_income, prediction))
        self.conn.commit()
        print("Prediction saved to database.")
obj = Database()
