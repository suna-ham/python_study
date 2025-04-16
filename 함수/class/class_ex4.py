class Car:
    speed = 0
    def upSpeed(self, value):
        self.speed = self.speed + value
        print("현재 속도(슈퍼클래스 부모클래스):%d"%self.speed)
class Sedan(Car):
    def __init__(self,value):
        self.upSpeed(value)
class Truck(Car):
    def __init__(self,value):
        self.upSpeed(value)

mySedan = Sedan(100)
myTruck = Truck(70)
