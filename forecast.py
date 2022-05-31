import requests

api_key = "7c33650d760502044f62892bc7edfb14"
city = "Helsinki"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

request = requests.get(url)
json = request.json()

description = json.get("weather")[0].get("description")
print("Today`s forecaast is", description)
temp_min = json.get("main").get("temp_min")
print("The minimum temperature is", temp_min, "Celcius degrees")
temp_max = json.get("main").get("temp_max")
print("The maximum temperature is", temp_max, "Celcius degrees")