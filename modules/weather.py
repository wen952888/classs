import requests

def get_weather(city):
    # Example API call to OpenWeatherMap (replace 'your_api_key' with your actual API key)
    api_key = "your_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "City not found"}