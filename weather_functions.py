import requests
from fuzzywuzzy import process

##weather-related functions here:
def fetch_weather_data(city):
    api_key = "75d9317487ef9e9f5f9e0125c20912c1"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.ConnectionError:
        return None

def suggest_clothing(temperature_celsius):
    if temperature_celsius > 30:
        return "It's very hot! Opt for shorts, a t-shirt, and a cap."
    elif 25 <= temperature_celsius <= 30:
        return "It's warm. A light shirt and shorts would be great."
    elif 18 <= temperature_celsius < 25:
        return "It's mild. Consider wearing jeans and a long-sleeve shirt."
    elif 10 <= temperature_celsius < 18:
        return "It's cool. A jacket or sweater would be comfortable."
    else:
        return "It's cold! Bundle up with a warm coat, scarf, and gloves."

def get_weather_tip(description):
    if "rain" in description.lower():
        return "Don't forget your umbrella!"
    elif "cloud" in description.lower():
        return "It might be a bit gloomy. A cup of hot-chocolate with friends would be fun!."
    elif "clear" in description.lower():
        return "Enjoy the clear sky. Consider using sun-lotin for protection!"
    else:
        return "Embrace the diverse weather! What adventure can you create today?"

def get_additional_tip(description):
    if "rain" in description.lower():
        return "How about making a paper boat and having a little race?"
    elif "clear" in description.lower():
        return "Perfect day for a picnic! Pack your favorite snacks."
    elif "snow" in description.lower():
        return "Build a snowman or have a snowball fight with friends!"
    elif "thunderstorm" in description.lower():
        return "Stay indoors and enjoy a cozy movie day with your favorite snacks."
    else:
        return "Explore the wonders of nature! Look for interesting plants,birds or insects."

def get_closest_city(user_input, cities_list, threshold=80):
    matches = process.extract(user_input, cities_list)
    closest_matches = [match[0] for match in matches if match[1] >= threshold]
    return closest_matches

def explain_humidity():
    print("\nHumidity is like how much water is in the air.")
    print(
        "If it's very humid, the air feels sticky and you sweat more!. If it's not humid, the air feels dry."
    )



def explain_wind_speed():
    print("\nWind speed is how fast the air is moving.")
    print(
        "If it's windy, you'll feel the air moving, it can be loud! If it's calm, the air is still."
    )


def explain_weather_terms():
   print("\nCurious to know the basic weather terms!")
   explain_humidity()
   explain_wind_speed()

# def get_background_image(description):
#     if "rain" in description.lower():
#         return "/static/rainy.jpg"
#     elif "snow" in description.lower():
#         return "/static/snowy.jpg"
#     elif "thunderstorm" in description.lower():
#         return "/static/thunderstorm.jpg"
#     else:
#         return "/static/images/AllSeasons.jpg"

def get_background_image(description, temperature_celsius):
    if "rain" in description.lower():
        return "/static/rainy.jpg"
    elif "snow" in description.lower():
        return "/static/snowy.jpg"
    elif "thunderstorm" in description.lower():
        return "/static/thunderstorm.jpg"
    elif temperature_celsius > 30:
        return "/static/rainy.jpg"
    elif 25 <= temperature_celsius <= 30:
        return "/static/thundrstrom.jpg"
    elif 18 <= temperature_celsius < 25:
        return "/static/snowy.jpg"
    elif 10 <= temperature_celsius < 18:
        return "/static/snowy.jpg"
    else:
        return "/static/rainy.jpg"
