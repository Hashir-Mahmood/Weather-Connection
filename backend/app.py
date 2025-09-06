from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
 
@app.route("/weather")
def weather():
    city = request.args.get("city", "London")
    api_key = os.getenv("WEATHER_API_KEY")

if __name__ == "__main__":