weather_condition = "맑음"
print(weather_condition)
temperature = 14
humidity = 34
wind_speed = 23
temperature_variation = 4
visivillity = 23
forecast = "눈"

print (temperature, humidity, wind_speed, temperature_variation, visivillity, forecast)

weather_condition = "비비"
print(weather_condition)
temperature = 14
humidity = 0.7
wind_speed = 23
temperature_variation = 4
visivillity = 23
forecast = "눈"

print (temperature, humidity, wind_speed, temperature_variation, visivillity, forecast)

#습도가 70%이상이면 위험하요 미만이면 안전해요
if( humidity >= 0.7):
    print("위험해요")
else:
    print("안전해요")

#바람의 속도가 50이상이면 위험해요 아니면 안전해요

if( wind_speed >= 50):
    print("위험해요")
else:
    print("안전해요")    

#기상예보가 비이면 우산이 필요해요 아니면 우산이 필요없어요
if(forecast == "비"): 
    print("우산이 필요해요")
else:
    print("우산이 필요없어요")

