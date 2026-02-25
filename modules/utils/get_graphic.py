from .get_weather import get_weather

def get_graphic(city_name: str):
    weather = get_weather(city_name, True)
    list_weather = weather.get("list")
    temperature_list = []
    min_temp = 100
    for weather in list_weather:
        temp = weather.get("main").get("temp")
        if temp < min_temp:
            min_temp = temp
        temperature_list.append(temp)
    round_temp = round(min_temp/5)*5
    min_show_temp = round_temp - 10
    list_temp = []
    for number in range(8):
        list_temp.append(min_show_temp + number * 5)
    list_height = []
    for temp in temperature_list:
        height = (temp - min_show_temp) * 2.874
        list_height.append(height)
    return list_temp, list_height



