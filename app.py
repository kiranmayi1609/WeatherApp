from flask import Flask, render_template, request
from fuzzywuzzy import process  # For string matching
from weather_functions import fetch_weather_data, suggest_clothing, get_weather_tip, get_additional_tip, get_closest_city,get_background_image

app = Flask(__name__,template_folder='templates')

# List of available cities
available_cities = [
    "",
        "Berlin",
        "Copenhagen",
        "Delhi",
        "Islamabad",
        "Istanbul",
        "Hamburg",
        "Oslo",
        "Stockholm",
        "New York",
        "Los Angeles",
        "Chicago",
        "Miami",
        "London",
        "Paris",
        "Tokyo",
        "Sydney",
    
]

@app.route('/')
def index():
    # city="London"
    # weather_data=fetch_weather_data(city)
    # description=weather_data["weather"][0]["description"] if weather_data else "Sunny"
    # background_image =get_background_image(description)
    # background_image=
    city = "London"  # Replace this with the city name you want to fetch weather for
    weather_data = fetch_weather_data(city)

    # Assuming the weather description and temperature are available in the fetched data
    description = weather_data["weather"][0]["description"] if weather_data else "Sunny"
    temperature_kelvin = weather_data["main"]["temp"] if weather_data else 293.15  # Replace with default temperature
    temperature_celsius = temperature_kelvin - 273.15

    # Get the appropriate background image based on the weather description and temperature
    background_image = get_background_image(description, temperature_celsius)
    return render_template('index.html', cities=available_cities,weather_info="Hello world",background_image=background_image)

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    weather_data = fetch_weather_data(city)

    if weather_data:
        temperature_kelvin = weather_data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        description = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]
        humidity = weather_data["main"]["humidity"]
        rain_chance = weather_data.get("rain", {}).get("1h", 0)  # 1-hour forecast for rain
        weather_info = {
            "city": city.capitalize(),
            "temperature": f"{temperature_celsius:.2f} °C",
            "wind_speed": f"{wind_speed} m/s",
            "humidity": f"{humidity}%",
            "rain_chance": f"{rain_chance}%",
            "clothing_suggestion": suggest_clothing(temperature_celsius),
            "weather_tip": get_weather_tip(description),
            "additional_tip": get_additional_tip(description)
        }
        
        return render_template('index.html', weather_info=weather_info)
    else:
        closest_matches = get_closest_city(city, available_cities)
        if closest_matches:
            return render_template('index.html', cities=available_cities, closest_matches=closest_matches)
        else:
            return render_template('index.html', cities=available_cities, not_found=True)

if __name__ == '__main__':
    app.run(debug=True)
