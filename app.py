from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
 
@app.route("/")
def weather():
    return render_template("index.html")

@app.route('/about')
def about():
    return "this is just empty"

if __name__ == "__main__":
    app.run(debug=True)