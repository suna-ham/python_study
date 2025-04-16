workplace_temp = 32.5
machine_vibration =6.8
last_accident_type ="기계오작동"
worker_heart_rate = 98
risk_detedcted= "True" #0 일때 True ??
workplace_humidity =78.2
risk_alert_count =12
detected_risks=70 #고온', '기계 과부하', '가스 누출'을 
system_status="active"
average_vehicle_speed =52.7


if (detected_risks >=80 and detected_risks <= 100 ):
    print("고온")
elif(detected_risks >=101 and detected_risks <=110):
    print("기계과부화")
elif(detected_risks <=111):
    print("가스누출")

