from config import *
from mysql import connector


class database_create:

    # Variable Initialisation

    def __init__(self):
        self.db = connector.connect(
        host=database_host,
        user=database_user,
        password=database_password,
        database=database_name)
        self.cursor = self.db.cursor(buffered=True,dictionary=True)



######################### Table Creation

    def feed_news(self):
        sql =(
            "CREATE TABLE IF NOT EXISTS Feed_News (" + 
            "ID MEDIUMINT NOT NULL UNIQUE AUTO_INCREMENT," +
            "Art TEXT," + 
            "Description TEXT," +
            "Title TEXT," +
            "TTitle TEXT," +
            "Author TEXT,"+
            "Link Text)" 
        )
            # Registration_Temp : ID | First_Name | Last_Name | Gender | Country | State | Username | Email | Hash | Password | Auth_Type | Verification | Join_Date

        self.cursor.execute(sql)
        self.db.commit()


    def feedback(self):
        sql =(
            "CREATE TABLE IF NOT EXISTS Feedback (" + 
            "ID MEDIUMINT NOT NULL UNIQUE AUTO_INCREMENT," +
            "Feedback TEXT," + 
            "Email TEXT," + 
            "Sent Date)"
        )
            # Registration_Temp : ID | First_Name | Last_Name | Gender | Country | State | Username | Email | Hash | Password | Auth_Type | Verification | Join_Date

        self.cursor.execute(sql)
        self.db.commit()


    def user(self):
        sql =(
            "CREATE TABLE IF NOT EXISTS user (" + 
            "id MEDIUMINT NOT NULL UNIQUE AUTO_INCREMENT," +
            "email TEXT NOT NULL UNIQUE," + 
            "password TEXT NOT NULL," +
            "first_name VARCHAR(64)," +
            "last_name VARCHAR(64)," + 
            "phone INT(64) UNIQUE," +
            "institute TEXT," +
            "degree TINYTEXT," +
            "branch TEXT," +
            "graduate_year INT(32)," +
            "type VARCHAR(64)," +
            "date_join DATE," +
            "qr_id MEDIUMINT UNIQUE," +
            "qr_date DATE," +
            "google_id TEXT UNIQUE)"
            
            
        )
            # user : id | email | password | first_name | last_name | phone | institution | degree | branch | graduate_year | type | date_join | qr_id | qr_date | google_id

        self.cursor.execute(sql)
        self.db.commit()

    def create_base(self):
        self.user()
        self.feed_news()
        self.feedback()



class call:
    
    # DB Manipulation

    def __init__(self):
        self.db = connector.connect(
        host=database_host,
        user=database_user,
        database=database_name,
        password=database_password)
        self.cursor = self.db.cursor(buffered=True,dictionary=True)
        print("sdf")

################### Actual Code Start Here

    def add_user(self, data):
        sql = (
                "INSERT INTO user " + 
                "(email, password, first_name, last_name, phone, institute, degree, branch, graduate_year, type, date_join, qr_id, qr_date, google_id)" + 
                "VALUE(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP(), %s, CURRENT_TIMESTAMP(), %s)"
                )
        quer = (  
            data["email"],
            data["password"],
            data["first_name"],
            data["last_name"],
            data["phone"],
            data["institute"],
            data["degree"],
            data["branch"],
            data["graduate_year"],
            data["type"],
            
            data["qr_id"],

            data["google_id"],
        )
        print(data)

        self.cursor.execute(sql, quer)
        self.db.commit()
