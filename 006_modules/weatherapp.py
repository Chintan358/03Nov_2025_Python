import requests

city = input("enter city name : ")
gresult = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid=f7e41ce7e70845cc2b06568cfc7cfb4c")

geocode  = gresult.json()


lat = geocode[0]['lat']
lon = geocode[0]['lon']
api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=f7e41ce7e70845cc2b06568cfc7cfb4c&units=metric"

result = requests.get(api)
data = result.json()
print(data['name'])
print("Temp : ",data['main']['temp'])