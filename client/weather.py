import json
import requests
import shutil

args = {'q': 'Liverpool', 'appid': '6ab080e35e3f41a6b81aeefc4d9de6a7'}
weather = requests.get('https://api.openweathermap.org/data/2.5/weather', params=args)

data = json.loads(weather.text)
#print(data)

print(data['weather'][0]['description'])

tempKelvin = data['main']['temp']
tempCelsius = tempKelvin - 273.15
tempCelsius = int(tempCelsius)
pressure = data['main']['pressure']
humidity = data['main']['humidity']

print(str(tempCelsius) + u"\u00B0C")
print(str(pressure) + " hPa")
print(str(humidity) + "%" + " humidity")

code = data['weather'][0]['icon']
img_url = "http://openweathermap.org/img/wn/" + code + "@2x.png"

icon = requests.get(img_url, stream=True)

img = open("weather.png", "wb")

icon.raw.decode_content = True

shutil.copyfileobj(icon.raw, img)

del icon
