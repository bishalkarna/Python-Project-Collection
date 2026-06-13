import requests

try:
    city_lat = 27.7172   # Kathmandu latitude
    city_lon = 85.3240   # Kathmandu longitude

    url = f"https://api.open-meteo.com/v1/forecast?latitude={city_lat}&longitude={city_lon}&current_weather=true"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    weather = data["current_weather"]

    print("\n--- Weather Report ---")
    print("Temperature:", weather["temperature"], "°C")
    print("Wind Speed:", weather["windspeed"], "km/h")
    print("Weather Code:", weather["weathercode"])

except requests.exceptions.RequestException:
    print("API request failed.")

except KeyError:
    print("Unexpected response format.")