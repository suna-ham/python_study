# n = 7
# n = float(n)
# print(type(n))

# n = input('번호를 입력하세요')

# n = input('번호를 입력하세요')
# n =int(n)

# height = input('키를 입력하세요')
# weight = input('몸무게를 입력하세요')

# height = float(height)
# weight = float(weight)

# bmi = weight / (height/100*height/100)
# bmi = float(bmi)
# print( bmi)
# print('bmi 지수는 '+ str(bmi) +'입니다.')

# 문제2)  연필과 펜의 구입하는 개수에 따라 총 가격을 반환해 주는 프로그램을 작성하세요

# -  연필 1000원 펜은 2000원 이다
# -  변수 num_pencil,  num_pen은 input()함수를 통해 각각 연필과 펜의 개수를 입력 받는다.
# -  변수 total_price는 총 가격을 나타낸다.
# -  총가격 = 연필의 갯수 * 1000 + 펜의 갯수 * 2000

# pencil = 1000
# pen = 2000
# num_pencil = input('연필 갯수를 입력해주세요 >')
# num_pen = input('펜의 갯수를 입력해주세요')
# num_pencil = int(num_pencil)
# num_pen =int(num_pen)
# total_price =(num_pencil*1000)+(num_pen*2000)

# print(total_price)
# 사용자가 x의 값을 입력하여 입력한 x만큼 @를 출력하는 프로그램
# num = input("숫자를 입력해주세요")
# double = (int(num)*"@")

# print(double)

# 사용자로부터 정수를 입력받아 그 숫자가 짝수인지 홀수인지를 출력하는 프로그램 작성하세요

num_x = input('숫자를 입력해주세요')

if(int(num_x)%2==0):
    print(str(num_x)+' 짝수입니다')
else:
    print(str(num_x)+' 홀수입니다')


# 사용자로부터 나이를 입력받아, 
# 19세 이상이면 "성인입니다."를 출력하고,
# 그렇지 않으면 "미성년자입니다."를 출력하는 프로그램을 작성하세요.

age = input('나이를 입력해주세요')

if(int(age)>=19):
 print('성인입니다')
else:
   print('미성년자입니다')

# 사용자로부터 비밀번호를 입력받고, 미리 설정된 비밀번호와 일치하면 "로그인 성공!",
#  일치하지 않으면 "비밀번호가 틀렸습니다."를 출력하는 프로그램을 작성하세요.

sever_pw = "!@#wer0"
input_pw = input('비밀번호를 입력해주세요')

if(sever_pw==input_pw):
   print('로그인 성공!')
else:
  print('비밀번호가 틀렸습니다.')

