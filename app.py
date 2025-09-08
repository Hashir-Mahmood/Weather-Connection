from flask import Flask, request, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("WEATHER_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    action = request.args.get("action")
    location = None
    temperature = None
    humidity = None
    wind_speed = None
    error = None
    
    if action == "search":
        city = request.args.get("q")
        if not city:
            error = "Please enter a city."
        else:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    location = data["name"]
                    temperature = round(data["main"]["temp"],1)
                    humidity = data["main"]["humidity"]
                    wind_speed = data["wind"]["speed"]
                else:
                    error = "Could not fetch weather data. Try another city."
            except requests.RequestException:
                error = "Network error. Please try again."
    
    elif action == "location":
        # For now: fallback static coordinates (Manchester)
        lat, lon = 53.4808, -2.2426
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                location = data["name"]
                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                wind_speed = data["wind"]["speed"]
            else:
                error = "Could not fetch weather by location."
        except requests.RequestException:
            error = "Network error. Please try again."
    
    return render_template(
        "index.html",
        location=location,
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed,
        error=error,
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)