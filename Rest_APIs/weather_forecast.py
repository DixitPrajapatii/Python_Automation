# City, Time , Temperature, Condition

import requests

def get_weather(city, units='metric', api_key='26631f0f41b95fb9f5ac0df9a8f43c92'):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  content = r.json()
  with open('./data.txt', 'a') as file:
    for data in content['list']:
      file.write(f"{data['dt_txt']}, {data['main']['temp']}, {data['weather'][0]['description']}\n")

print(get_weather(city='tokyo'))