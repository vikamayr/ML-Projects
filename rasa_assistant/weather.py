import requests

def Weather(city):
    print("value for city:", city)
    API_key='e64c53e3b2af48cc09b1dceb198bbb67'
    api='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    url=api.format(city, API_key)
    
    json_data = requests.get(url).json()
    main_data = json_data['main']
    
    weather_response ="The weather in {0} is {1}. The temperature is {2} Celsius and feels like {3} Celsius.".format(
        city,
        json_data['weather'][0]['description'],
        int(main_data['temp']-273.15),
        int(main_data['feels_like']-273.15))
  
    return weather_response