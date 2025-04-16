# a = True
# print(type(a))

# a = False
# b = a
# print(type(b))
# print(b, a)

# n = input('숫자입력하기')
# flag = int(n) % 2
# print(flag == 1)

# - 상대방의 키(your_height)가 나(my_height)보다 작은지 확인한다.  your_height < my_height
# -  그 남자의 혈액형이 B형이 아니면  blood_type != 'B'
# 나보다 작군요, 나보다 크군요, 나와같군요

# my_height = input('나의 키를 입력하세요요')
# your_height =input('비교자의의 키를 입력하세요 >')

# if(int(my_height )== int(your_height)):
#     print("나와같군요")
# elif(int(my_height)>=int(your_height)):
#     print("나보다 작군요")
# elif(int(my_height)<=int(your_height)):
#     print("나보다 크군요")

need_blood = "B"
input_blood = input('혈액형을 입력하세요 >')

view_blood = input_blood.upper()

if(need_blood == view_blood):
    print('당신은 B형이군요 지금 필요한 혈액형입니다 헌혈하세요')
else:
    print('당신은 '+view_blood+'형이군요 헌혈하지 않아도 돼요')

# 문제2) 백화점 상품권

# 요구사항 
# 길동이는 백화점에서 여러 물건을 구매하였다. 상품권을 받을 수 있는 지 판단하는 프로그램 

# 상품권 받을 수 있는 조건
# 구매한 모든 물품의 총합이 10만원 이상이면 상품권을 받을 수 있다

# 길동이가 구매한 물품 가격은 30000, 50000, 15000, 25000

p1 = int(input("상품의 가격을 입력해주세요"))
p2 = int(input('상품의 가격을 입력해주세요'))
p3 = int(input('상품의 가격을 입력해주세요'))
p4 = int(input('상품의 가격을 입력해주세요'))

sum = p1+p2+p3+p4

if(sum>=100000):
    print('상품권을 수령하세요')
else:
    minus = 100000 - sum
    print(str(minus)+'원만 더 구해사히면 상품권이 지급됩니다')


# 구매한 물건의 갯수를 입력받음
num_items = int(input("구매한 물건의 갯수를 입력해주세요: "))

total = 0

# 입력한 갯수만큼 반복하며 각 상품의 가격을 누적
for i in range(num_items):
    price = int(input(f"상품 {i+1}의 가격을 입력해주세요: "))
    total += price

# 누적한 총합에 따라 결과 출력
if total >= 100000:
    print("상품권을 수령하세요")
else:
    remaining = 100000 - total
    print(f"{remaining}원만 더 구해사히면 상품권이 지급됩니다")

