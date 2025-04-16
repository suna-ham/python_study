# 문제1)  math 모듈 사용하기
# 반지름이 5인 원의 넓이를 구하세요.
# 힌트: math 모듈의 pi와 pow 함수를 사용하세요.
import math

r = 5

one = math.pi*math.pow(r,2)
print(one)

# 문제2) random 모듈로 숫자 뽑기

# 1부터 100 사이의 숫자 중 랜덤으로 1개를 출력하는 코드를 작성하세요.
# 힌트: random.randint() 함수를 사용해 보세요.

import random

# num = list(range(1,101))
# print(random.randrange(1,101))
print(random.randint(1,100))

# 문제3) datetime 모듈로 현재 날짜 구하기

# 오늘 날짜를 YYYY-MM-DD 형식으로 출력하세요.
# 힌트: datetime 모듈과 strftime()을 활용해 보세요.
import datetime

today = datetime.datetime.today()
print(today.strftime("%Y-%m-%d"))

from datetime import datetime

today = datetime.now()
print(today.strftime("%Y-%m-%d"))