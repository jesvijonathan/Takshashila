from flask import Flask

from routes.userRoute import userRoute
from database import Database,db

app = Flask(__name__)
app.secret_key='dvdf'

Database(app)

@app.before_first_request
def create_tables():
    db.create_all()

app.register_blueprint(userRoute)

if __name__=='__main__':
    app.run(debug=True)