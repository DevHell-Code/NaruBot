from threading import Thread
from flask import Flask,request,render_template,session,redirect
from oauth import Oauth

app = Flask(__name__)
app.config["SECRET_KEY"] = "PRIVATE"

@app.route("/")
def home():
    return "test"

@app.route("/login")
def login():
    code = request.args.get("code")
    app.logger.info(code)
    at = Oauth.get_access_token(code)
    session["token"] = at

    user = Oauth.get_user_json(at)
    user_name, user_id = user.get("username"), user.get("discriminator")
    print("웨안됌")
    print(user_name)
    return "hello"

def run():
    app.run(host='0.0.0.0', port=80)

def keep_alive():
    t = Thread(target=run)
    t.start()