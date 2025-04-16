class Car :
    color =""
    price = 0
    speed =0
    #생성자
    def __init__(self, *v1):
        if 
        self.color = v1[0]
        self.price = v1[1]
        self.speed = v1[2]

myCar =Car("빨강", 1000,40)
myCar2 =Car("파랑", 1000)



class Car:
    #멤버필드
    color =""
    price = 0
    speed = 0
    # 생성자
    def __init__( self, *v1):
        for i in range( len(v1) ) :
           if( i==0):
              self.color = v1[0]
           if (i==1):
              self.price = v1[1]
           if (i==2) :
              self.speed = v1[2]
myCar =Car( "빨강", 1000, 30  )
print(myCar.color, myCar.price, myCar.speed) 
myCar2 =Car( "파랑", 2000  )
print(myCar2.color, myCar2.price, myCar2.speed) 
myCar3 =Car( "노랑"  )
print(myCar3.color, myCar3.price, myCar3.speed) 

