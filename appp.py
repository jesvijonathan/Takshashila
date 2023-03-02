from flask import Flask, redirect, url_for, session
from flask_dance.contrib.google import make_google_blueprint, google
import os

app = Flask(__name__)
app.secret_key = "mysecretkey"

blueprint = make_google_blueprint(
    client_id="562058780483-q59qv7347cgqujgebrsf15n6b0u8uhmq.apps.googleusercontent.com",
    client_secret="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",
    redirect_url= "http://127.0.0.1:5000",
    scope = 'openid https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile'  
)

app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    print(resp.json())
    email = resp.json()["email"]
    return f"Logged in as {resp.json()}"


@app.route("/nig")
def cock():
    if not google.authorized:
        return "NOT LOGGED"
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    print(resp.json())
    email = resp.json()["email"]
    return f"Logged in as {resp.json()}"

if __name__ == "__main__":
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' 
    app.run()