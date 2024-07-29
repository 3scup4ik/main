open_weather_token = "5d4bdde7085a8d3791cef772e602ea40"
import requests
from pprint import *
def weather(city, open_weather_token):
    try:
        req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}")
        data=req.json()
        pprint(data)
    except exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    city = input("Введите город:")
    weather(city,open_weather_token)

if __name__=="__main__":
    main()
