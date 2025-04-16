n =input('번호를 입력하세요 >>')
print(n)

#문제
#번호를 입력하세요?25
#이름을 입력하세요? 홍길동
#나이를 입력하세요? 23
#25번 홍길동씨의 나아니는 23살 입니다.

# num =input('번호를 입력하세요 >')
# print(num)
# name =input('이름을 입력하세요 >')
# print(name)
# age =input('나이를 입력하세요 >')
# print(age)

# print(num +"번", name +"씨의 나이는 ", age + "입니다.")

#  if (num and name and age)
#      print(num +"번" name +"씨의 나이는 " age + "입니다.")

#문제
# 이름은 홍길홍
# 점수는 80
# 학점은 3학점
# 홍길동씨의 점수 80점이고 3학점입니다

# hname =input('이름을 입력하세요 >')
# hscore =input('점수를 입력하세요 >')
# hgrade =input('학점을 입력하세요 >')

# print(hname +"씨의 점수 "+ hscore+"점 이고"+ hgrade+"학점입니다.")



hname =input('이름을 입력하세요 >')
hscore =input('점수를 입력하세요 >')

if(hscore >= 0 and hscore  <= 50):
    print(type(hscore))
elif(hscore >= 51 and hscore  <= 70):
    print(type(hscore))
elif(hscore >= 71 and hscore  <= 90):
    print(type(hscore))
elif(hscore >= 91 and hscore  <= 100):
    print( type(hscore))
# 자료형을 str에서 int로 바꿔줘

hscore = int(hscore)
print(type(hscore))

# if(hscore >= 0 and hscore  <= 50):
#     grade ="F"
# elif(hscore >= 51 and hscore  <= 70):
#     grade ="C"
# elif(hscore >= 71 and hscore  <= 90):
#     grade ="B"
# elif(hscore >= 91 and hscore  <= 100):
#     grade ="A"

# print(hname +"씨의 점수 "+ hscore+"점 이고"+ grade + "학점입니다.")
