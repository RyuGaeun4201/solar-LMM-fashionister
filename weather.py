import requests
import json
 
city = "Seoul"
apikey = "8a50fb88531f6edcb8703106d30a4c45"
lang = "kr"

api = f"""http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"""
 
result = requests.get(api)
 
data = json.loads(result.text)
 
print(data)