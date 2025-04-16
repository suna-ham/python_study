# age = 10
# if( age >=6 and age<=12) :
#     passenger_type="어린이"
#     fare = 700
# elif( age >=13 and age<=18) :
#     passenger_type="청소년"
#     fare = 1100
# elif( age<18) :
#     passenger_type="어른"
#     fare = 1500

#     print(passenger_type+"의 버스요금은" +str(fare)+ '원 입니다.')

# 문제1) 어느 놀이 공원에서는 여자 신입생에게는 20% 할인 혜택을 제공한다고 한다.
# 수지는 여자이고 2학년이다. 수지가 혜택을 받을 수 있는가? 

# name = input('이름을 입력하세요')
# grade = int(input('몇 학년인가요?')) #숫자값으로 받아야 비교가능!
# gender = input('성별을 입력하세요')

# benefit_grade = 1
# benefit_gender = "여"

# if ( grade == benefit_grade and gender == benefit_gender):
#     print(name +'은(는) 할인혜택 대상입니다')
# else:
#     print('할인혜택 대상이 아닙니다')

# 어느 회사의 입사조건은 토익점수가 800점 이상이거나 교양영어에서 A학점이 만족해야 지원 가능하다고 한다.
# 길동이는 토익이 900점이고 교양 영어는 B학점이다 길동이는 이 회사에 지원할 수 있는가?


# toeic = int(input('토익점수를 입력해주세요'))
# liberal= input('교양 학점을 입력해주세요')

# if(toeic >= 800 or liberal.upper() == "A" ):
#     print("응시가능")
# else:
#     print('응시불 가능')

# 문제3) 하나에 1000원하는 연필과 하나에 2000원하는 펜이 있다. 구입시 10000원이 넘으며 10%을 해준다.
# 구매하고자하 하는 연필과 펜의 개수를 사용자로부터 입력 받는다
# 조건문을 활용하여 할인율을 적용한다

pencil = int(input('구매한 연필의 갯수를 입력하세요'))
pen = int(input('구매한 펜의 갯수를 입력하세요'))

p1 = pencil*1000
p2 = pen*2000

if(p1+p2 > 10000 ):
    print( "10%로 할인되어" + str((p1+p2)-(p1+p2)*0.1) + "원 입니다")
else:
    (p1+p2) <= 10000
    print(str(p1+p2)+"원 입니다")

# 선생님 코드 영수증 st
print("페이펄문구 계산")
pencil=int(input("연필갯수?"))
pen = int(input("펜갯수?"))
price=pencil * 1000 + pen * 2000
print("할인전금액 :" + str(price))
if( price >= 10000):
    sale = price * 0.1
    price = price - price*0.1
print("할인금액 : " + str(sale) )
print("판매금액 :" + str(price))