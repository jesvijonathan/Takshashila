from config import *
from mysql import connector


class database_create:

    # Variable Initialisation

    def __init__(self, cursorr, dbr):
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
            "CREATE TABLE IF NOT EXISTS uiser (" + 
            "ID MEDIUMINT NOT NULL UNIQUE AUTO_INCREMENT," +
            "Feedback TEXT," + 
            "Email TEXT," + 
            "Sent Date)"
        )
            # Registration_Temp : ID | First_Name | Last_Name | Gender | Country | State | Username | Email | Hash | Password | Auth_Type | Verification | Join_Date

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


    def get_db(self):
        sql = (
            "SHOW DATABASES"
            )

        self.cursor.execute(sql)

        return self.cursor.fetchall()


    def get_tbl(self,sel_db):
        sql = (
            "USE {0}".format(sel_db)
            )

        self.cursor.execute(sql)
        self.db.commit()

        sql_1 = (
            "SHOW TABLES"
            )

        self.cursor.execute(sql_1)

        return self.cursor.fetchall()


    def get_table(self,name):
        sql = (
                "SELECT * FROM {0}".format(name)
            )

        self.cursor.execute(sql)

        return self.cursor.fetchall()



#insert cmd example
    def add_user(self, user):
        username = user['username']
        first_name = user['first_name']
        last_name = user['last_name']

        sql = (
            "INSERT INTO user_base (user_id, username, first_name, last_name, is_bot, date) VALUE(%s, %s, %s, %s, %s, CURRENT_TIMESTAMP()) ON DUPLICATE KEY UPDATE username=%s, first_name=%s, last_name=%s")
        data = (
            user['id'],
            username, first_name, last_name,
            user['is_bot'],

            username, first_name, last_name,
        )

        self.cursor.execute(sql, data)
        self.db.commit()


#select cmd example
    def get_user(self, user_id=None):
        if user_id == None:
            sql = (
            "select * FROM user_base"
            )

            data = ()
        else:
            sql = (
                "SELECT * FROM user_base WHERE user_id=%s"
            )

            data = (
                user_id,
            )

        self.cursor.execute(sql, data)

        return self.cursor.fetchall()


#update cmd example
    def add_link(self, chat, user, status="member", replace=0):
        chat_id = chat['id']
        user_id = user['id']

        sql = (
            "SELECT (1) FROM link_base WHERE chat_id=%s AND user_id=%s LIMIT 1"
        )
        data = (
            chat_id,

            user_id
        )
        # print(data)

        self.cursor.execute(sql, data)

        if self.cursor.fetchone():
            if replace == 1:
                sql1 = (
                    "UPDATE link_base SET status=%s, last_active=CURRENT_TIMESTAMP() WHERE chat_id=%s AND user_id= %s LIMIT 1"
                )
                data1 = (
                    status, chat_id, user_id
                )
            else:
                sql1 = (
                    "UPDATE link_base SET last_active=CURRENT_TIMESTAMP() WHERE chat_id=%s AND user_id= %s LIMIT 1"
                )
                data1 = (
                    chat_id, user_id
                )
        else:
            sql1 = (
                "INSERT INTO link_base (chat_id, user_id, status, join_date, last_active) VALUE(%s, %s, %s, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP())"
            )
            data1 = (
                chat_id, user_id, status
            )

        self.cursor.execute(sql1, data1)
        self.db.commit()


################### Actual Code Start Here
def add_user(self, user):
    sql = (
            "INSERT INTO user " + 
            "(email, password, first_name, last_name, phone, institute, department, type, date_join, qr, date_qr, google_id)" + 
            "VALUE(%s, %s, %s, %s, %s, CURRENT_TIMESTAMP())" +
            "ON DUPLICATE KEY UPDATE username=%s, first_name=%s, last_name=%s")
    data = (  
    )

    self.cursor.execute(sql, data)
    self.db.commit()
