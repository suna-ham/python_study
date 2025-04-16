driver_speed = 200 #운전속도
lane_change_frequency = 2 #차선변경빈도
braking_intentity = 1 #급제동 사용시 1 비사용시 0 
acceleration= 40 #가속도
smartphone_usage= 0 # 운전중 스마트폰사용 사용시 1 비사용시 0

#차선변경빈도 3회 이상이면 운전습관 "나쁜운전습관"
#스마트폰 사용하면 운전습관 "나쁜운전습관"
#급제동하면 "나쁜운전습관"


if (lane_change_frequency >=3):
    print("나쁜 운전습관")
if(smartphone_usage == 1):
    print("나쁜운전습관")
if(braking_intentity == 1):
    print("나빠요요")


if (lane_change_frequency >=3 and smartphone_usage == 1 and braking_intentity == 1):
    print("매우 나쁜 운전습관")
if (lane_change_frequency >=3 or smartphone_usage == 1 or braking_intentity == 1):
    print("주의가 필요해요")

#속도 0~50저속주행 51~75 보통주행 76~199 고속주행 101 이상이면 과속주행

if(driver_speed >=0 and driver_speed <=50):
#if(0<= driver_speed <=50):  파이썬에서만 0
    print("저속주행")
elif(driver_speed >=51 and driver_speed <=75):
    print("보통주행")
elif(driver_speed >=76 and driver_speed <=100):
    print("고속주행")
# else(driver_speed >=101):
#    print("과속주행")
else:
    print("과속주행")

