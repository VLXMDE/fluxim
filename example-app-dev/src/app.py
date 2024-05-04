from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "fluxim 0.0.2"