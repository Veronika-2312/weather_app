import requests

api_key = "9c849885d6a2987db9da3ffb0dc061c8"
def get_weather(city_name:str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
        
