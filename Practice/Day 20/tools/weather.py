import requests


def get_weather(city):
    try:
        # Step 1: Find city coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=10
        )

        geo_response.raise_for_status()

        geo_data = geo_response.json()

        if "results" not in geo_data or not geo_data["results"]:
            return {
                "success": False,
                "error": f"City '{city}' not found."
            }

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        country = location.get("country", "")

        # Step 2: Get current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "apparent_temperature,"
                "precipitation,"
                "wind_speed_10m"
            ),
            "timezone": "auto"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=10
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()
        current = weather_data["current"]

        return {
            "success": True,
            "city": city_name,
            "country": country,
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "feels_like": current["apparent_temperature"],
            "precipitation": current["precipitation"],
            "wind_speed": current["wind_speed_10m"],
            "unit": "°C"
        }

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Weather API request timed out."
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"Weather API error: {str(e)}"
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        }


if __name__ == "__main__":

    city = input("Enter city name: ")

    result = get_weather(city)

    if result["success"]:

        print("\nCurrent Weather")
        print("=" * 40)

        print("City:", result["city"])
        print("Country:", result["country"])
        print("Temperature:", result["temperature"], result["unit"])
        print("Feels Like:", result["feels_like"], result["unit"])
        print("Humidity:", result["humidity"], "%")
        print("Precipitation:", result["precipitation"], "mm")
        print("Wind Speed:", result["wind_speed"], "km/h")

    else:
        print("\nError:", result["error"])