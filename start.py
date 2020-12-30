from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello From flask>start.py file..."