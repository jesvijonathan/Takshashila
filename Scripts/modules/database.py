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

    # Table Creation

    # def artist_base(self):
    #     sql = (
    #         "CREATE TABLE IF NOT EXISTS Artist_Base ( Artist_ID VARCHAR(14) PRIMARY KEY, User_ID INT(11), Artist_Name TEXT, Name TEXT, Artist_Links LONGTEXT, Artist_Assets TEXT)"
    #     )  #  Artist_Base : Artist_ID | User_ID | Artist_Name | Name | Artist_Links | Artist_Assets

    #     self.cursor.execute(sql)
    #     self.db.commit()

    def feed_base(self):
        sql = (
            "CREATE TABLE IF NOT EXISTS Feed_Base (ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, Title TEXT, Topic TEXT, Description LONGTEXT, Author TEXT, Link TEXT)"
        )  #  Feed_Base : Feed_id | Title | Topic | Description | Author | Link

        self.cursor.execute(sql)
        self.db.commit()



########################

    def album_base(self):
        sql = (
            "CREATE TABLE IF NOT EXISTS Album_Base (" + 

            "ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY," + 
            "UPC INT(32) UNIQUE NOT NULL," +
            "ISRC VARCHAR(32) NOT NULL," +
            "Title TEXT NOT NULL," +
            "Album_Version TEXT," + 
            "Compilation_Album Boolean Default 0," + 
            "Genre Text," +
            "Composition_Copyright TEXT NOT NULL," +
            "Sound_Recording_Copyright TEXT NOT NULL," +
            "Label TEXT Default 'Cepher Records'," + 
            "Original_Release_Date DATE NOT NULL,"+ 
            "Pre_Order_Date DATE," +
            "Sales_Start_Date DATE NOT NULL," +
            "Language TEXT Default 'None'," + # none - no lang
            "Explicit VARCHAR(14) Default 0)" # 1 not exp, 2 exp, 3 - clean
        )   

            # Album_Base : ID | ISRC | UPC | Title | Album_Version | Compilation_Album | Genre | Composition_Copyright | Sound_Recording_Copyright | Label | Original_Release_Date | Sales_Start_Date | Pre_Order_Date | Language | Explicit

        self.cursor.execute(sql)
        self.db.commit()

    def music_base(self):
        sql = (
            "CREATE TABLE IF NOT EXISTS Music_Base (" +

            "ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY," + 
            "ISRC VARCHAR(32) UNIQUE NOT NULL," + 
            "Title TEXT NOT NULL," + 
            "Title_Version TEXT," +
            "Track_Number INT(14) NOT NULL," +
            "Audio_Language TEXT  Default 'None'," + # none - no lang
            "Explicit VARCHAR(14)  Default 0)" # 1 not exp, 2 exp, 3 - clean
        )   

            # Music_Base : ID | ISRC | Title | Title_Version | Track_Number | Audio_Language | Explicit
            # genre | duration | format | file_name

        self.cursor.execute(sql)
        self.db.commit()

    def artist_base(self):
        sql =(
            "CREATE TABLE IF NOT EXISTS Artist_Base (" +

            "ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY," + 
            "User_ID INT(32) NOT NULL," +  
            "Artist_Name TEXT NOT NULL," + 
            "On_Spotify VARCHAR(32)," +  
            "Social_Website TEXT," +  
            "Social_Picture TEXT," +
            "Social_Spotify LONGTEXT," +
            "Social_Artist LONGTEXT," + 
            "Social_Soundcloud LONGTEXT," +
            "Social_Youtube LONGTEXT," +
            "Social_Instagram LONGTEXT," +
            "Social_Twitter LONGTEXT," +
            "Social_Facebook LONGTEXT," +
            "Description LONGTEXT," +
            "Join_Date DATE NOT NULL)"
        )
            # Artist_Base : ID | Name | User_ID | Unique_Artist_Links | Socials

        self.cursor.execute(sql)
        self.db.commit()

    def user_base(self):
        sql =(
            "CREATE TABLE IF NOT EXISTS User_Base (" + 
            "ID MEDIUMINT NOT NULL UNIQUE AUTO_INCREMENT," +
            "SHAID VARCHAR(512) NOT NULL UNIQUE PRIMARY KEY," + 
            "First_Name TEXT NOT NULL," + 
            "Last_Name TEXT," +
            "Gender VARCHAR(64)," + 
            "Country_Code VARCHAR(32)," + 
            "Phone VARCHAR(128)," +
            "Newsletter VARCHAR(32)," +
            "Username TEXT UNIQUE NOT NULL," +
            "Email TEXT UNIQUE NOT NULL," +
            "Hash LONGTEXT UNIQUE NOT NULL," + 
            "Password TEXT NOT NULL," + 
            "Auth_Type INT(14) NOT NULL DEFAULT 0," +  # 0 - email login, 1- google auth
            "Join_Date DATE NOT NULL)"
        )
            # User_Base : ID | First_Name | Last_Name | Gender | Country | State | Username | Email | Hash | Password | Auth_Type | Join_Date

        self.cursor.execute(sql)
        self.db.commit()

    def artist_link(self):
        sql =(
            "CREATE TABLE IF NOT EXISTS Artist_Link (" +

            "ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY," + 
            "UPC INT(32) NOT NULL," +
            "ISRC VARCHAR(32) NOT NULL," + 
            "Artist_ID INT(32) NOT NULL," + 
            "Role TEXT NOT NULL)"
        )
            # Artist_Link_Base : ID | UPC | ISRC | Artist_ID | Role

        self.cursor.execute(sql)
        self.db.commit()
    
    def music_link(self):
        sql =(
            "CREATE TABLE IF NOT EXISTS Music_Link (" +

            "ID MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY," + 
            "UPC INT(32) NOT NULL," + 
            "ISRC VARCHAR(32) NOT NULL," +
            "Art_Link TEXT," + 
            "External_Link TEXT," + 
            "Links LONGTEXT)"
        )
            # Music_Link : ID | UPC | ISRC | Art_Link | External_Link | Links

        self.cursor.execute(sql)
        self.db.commit()

    def video_base(self):
        sql = (
            "CREATE TABLE IF NOT EXISTS Video_Base (" + 
            "Video_ID VARCHAR(32) PRIMARY KEY," +
            "Title TEXT," + 
            "Artist TEXT," +
            "Channel TEXT," +
            "Publish_Date Date," + 
            "Thumbnail TEXT," + 
            "Is_Music_Video BOOL," + 
            "UPC INT(32)," + 
            "ISRC VARCHAR(32)," +
            "Artist_ID INT(32)," + 
            "Link TEXT)"
        )  #  Video_Base : Video_ID | Title | Artist_ID | Link | Channel | Thumbnail | Date
        
        self.cursor.execute(sql)
        self.db.commit()

    def register(self):
        sql =(
            "CREATE TABLE IF NOT EXISTS Registration_Temp (" + 
            "ID MEDIUMINT NOT NULL UNIQUE AUTO_INCREMENT," +
            "SHAID VARCHAR(512) NOT NULL UNIQUE PRIMARY KEY," +
            "First_Name TEXT NOT NULL," + 
            "Last_Name TEXT," + 
            "Gender VARCHAR(64)," + 
            "Country_Code VARCHAR(32)," + 
            "Phone VARCHAR(128)," +
            "Newsletter VARCHAR(32)," +
            "Username TEXT UNIQUE NOT NULL," +
            "Email TEXT UNIQUE NOT NULL," +
            "Hash LONGTEXT UNIQUE NOT NULL," +
            "Password TEXT NOT NULL," +
            "Auth_Type INT(14) DEFAULT 0," + # 0 - email login, 1- google auth
            "Verification BOOLEAN DEFAULT 0," +
            "Join_Date DATE NOT NULL)"
        )
            # Registration_Temp : ID | First_Name | Last_Name | Gender | Country | State | Username | Email | Hash | Password | Auth_Type | Verification | Join_Date

        self.cursor.execute(sql)
        self.db.commit()

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




    def create_base(self):
        self.album_base()
        self.music_base()
        self.artist_base()
        self.user_base()
        self.artist_link()
        self.music_link()
        self.register()

        self.feedback()

        self.feed_news()
        self.video_base()

        # to do, user base get input, (auth or email)
        # user base to artist base link (via pkey)
        
        # get album
        # get music details (from gform embedd)
        # link musci

        # link artist to music (using form, and isrc))

        
########################

    def video_base(self):
        sql = (
            "CREATE TABLE IF NOT EXISTS Video_Base ( Video_ID VARCHAR(14) PRIMARY KEY, Title TEXT, Artist TEXT, Channel TEXT, Publish_Date Date, Thumbnail TEXT, Link TEXT)"
        )  #  Video_Base : Video_ID | Title | Artist_ID | Link | Channel | Thumbnail | Date
        
        self.cursor.execute(sql)
        self.db.commit()


class call:
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
        # print(data)

        self.cursor.execute(sql, data)
        self.db.commit()


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



    def add_chat(self, chat):
        title = chat['title']
        username = chat['username']

        sql = (
            "INSERT INTO chat_base (chat_id, type, title, username, join_date) VALUE(%s, %s, %s, %s, CURRENT_TIMESTAMP()) ON DUPLICATE KEY UPDATE title=%s, username=%s")
        data = (
            chat['id'], chat['type'],
            title, username,

            title, username
        )
        # print(data)

        self.cursor.execute(sql, data)
        self.db.commit()


    def get_chat(self, chat_id=None):
        if chat_id == None:
            sql = (
                "SELECT * FROM chat_base"
            )

            data = ()
        else:
            sql = (
                "SELECT * FROM chat_base WHERE chat_id=%s"
            )

            data = (
                chat_id,
            )

        self.cursor.execute(sql, data)

        return self.cursor.fetchall()



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


    def get_link(self, chat_id=None, user_id=None):
        if chat_id == None and user_id == None:
            sql = (
            "SELECT * FROM link_base"
            )

            data = ()
        else:
            sql = (
                "SELECT * FROM link_base WHERE chat_id=%s AND user_id=%s"
            )

            data = (
                chat_id, user_id,
            )

        self.cursor.execute(sql, data)

        return self.cursor.fetchall()


    def add_settings(self, chat_id, members):

        sql = (
            "INSERT INTO settings_base (chat_id, members) VALUE(%s, %s) ON DUPLICATE KEY UPDATE members=%s"
        )
        data = (
            chat_id, members,
            members
        )

        # print(data)

        self.cursor.execute(sql, data)
        self.db.commit()


    def get_settings(self, chat_id=None):
        if chat_id == None:
            sql = (
                "SELECT * FROM settings_base"
            )

            data = ()
        else:
            sql = (
                "SELECT * FROM settings_base WHERE chat_id=%s"
            )

            data = (
                chat_id,
            )

        self.cursor.execute(sql, data)

        return self.cursor.fetchall()


    def add_welcome(self, chat_id, welcome_text="Hello {first_name}, \nWelcome to {group_name} !"):

        sql = (
            "REPLACE INTO welcome_base (chat_id, welcome_text) VALUE(%s, %s)"
        )
        data = (
            chat_id, welcome_text
        )

        # print(data)

        self.cursor.execute(sql, data)
        self.db.commit()


    def get_welcome(self, chat_id=None):
        if chat_id==None:
            sql = (
                "SELECT * FROM welcome_base"
            )

            data = ()
        else:
            sql = (
                "SELECT * FROM welcome_base WHERE chat_id=%s"
            )

            data = (
                chat_id,
            )

        self.cursor.execute(sql, data)

        return self.cursor.fetchall()
