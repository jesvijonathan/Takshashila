from flask import Flask, redirect, url_for, session
from flask_dance.contrib.google import make_google_blueprint, google
import os

app = Flask(__name__)
app.secret_key = "mysecretkey"

blueprint = make_google_blueprint(
    client_id="562058780483-q59qv7347cgqujgebrsf15n6b0u8uhmq.apps.googleusercontent.com",
    client_secret="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",
    redirect_url= [
      "http://127.0.0.1:5000",
      "http://127.0.0.1:5000/auth/callback",
      "http://127.0.0.1:5000/auth/oauth_redirect",
      "https://takshashila.pythonanywhere.com",
      "https://takshashila.pythonanywhere.com/auth/callback",
      "https://takshashila.pythonanywhere.com/auth/oauth_redirect"
    ],
    scope=["profile", "email"],
)

app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email = resp.json()["email"]
    return f"Logged in as {email}"

if __name__ == "__main__":
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    app.run()