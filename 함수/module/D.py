from module1 import func3#module1의 파일의 특정함수만 가져오기
from module1 import * #module1의 파일의 모든함수 가져오기
import sys
import math
import time



print(sys.builtin_module_names)

func3()
print(math.log(10))
print(math.sin(30))
list_1 =[10,50,77,90]
print(math.fsum(list_1))
a = 3
#거듭제곱의 값
print(math.pow(a,5))
print(math.pi)

utc=time.time()#UTC시간
print(time.gmtime(utc))
tm=time.gmtime(utc)
print("현재년도 : ", tm.tm_year )
print("현재 월 : " , tm.tm_mon )
print("현재 일 : " , tm.tm_mday )
print("현재 시 : " , tm.tm_hour)
print("현재 분 :", tm.tm_min)
print("현재 초 :", tm.tm_sec)

string = time.ctime(time.time())

string = time.strftime("%Y-%M-%d %I:%M:%S %p", tm)
print(string)

import datetime
today = datetime.date.today()
print( today )