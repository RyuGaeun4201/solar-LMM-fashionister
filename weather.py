import requests
import json
 
city = "Seoul"
apikey = "8a50fb88531f6edcb8703106d30a4c45"
lang = "kr"

api = f"""http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"""
 
result = requests.get(api)
 
data = json.loads(result.text)

def range_temp(temp):
    if temp<10: 
        temp_str= '엄청 추움'
    elif temp<20:
        temp_str= '추움'
    elif temp<30:
        temp_str= '선선'
    else:
        temp_str='더움'
    
    return temp_str

def temp_diff(temp_diff):
    if temp_diff>10:
        return '큰 일교차'
    else:
        return '작은 일교차'
    
def humidity(humdity):
    if humdity>85:
        return '우천 예보'
    else:
        return '우천 예보 없음'
    
def cloud(cloud):
    if cloud>90:
        return '구름이 많다'
    elif cloud<20:
        return '쨍쨍'
    else:
        return '구름 조금'
    
def wind(wind):
    if wind>7:
        return '강풍'
    else:
        return '강풍 예보 없음'

def weather() :
    return f"{range_temp(data['main']['temp'])}, {temp_diff(data['main']['temp_max']-data['main']['temp_min'])}, {humidity(data['main']['humidity'])}, {cloud(data['clouds']['all'])}, {wind(data['wind']['speed'])}"
