list1 =[10, 20,'red',12.43]
list2 =[]
list3 =['a', [1,2,3]]
list3 =['a', [1,2,3,['c', 'b']]]
list4 =[100,[True, False], 200, 300]
print(list3[1][2], list3[1])
print(list3[1][3][0])

print(list4[2])
print(list4[1])

# 4 3 2 1 출력하기
a =[1, 2, 3, 4]

print(a[-1], a[-2], a[-3], a[-4])


# 4) list형의 원소에 접근할 때 int형의 index를 쓸수도 있지만 덧셈, 뺄셈, 곱셈, 나머지 연산을 사용할 수 도 있다.
# 이 때 연산의 결과값은  반드시 list형이 되어야 한다.
# 실습 list 내역을 연산으로 표현가능)

list_ex = [5,9,301,714,3776, 9614]
high =6 
low=3
print(list_ex[3+2])
print(list_ex[high-low])
# print(list_ex[2*2.5]) 실수형은 안됨 not float
print(list_ex[5%4])

# 문제) 
numlist = [0,10,20,30,40,50,60,70,80,90]
temp = 3

# numlist에서 temp 값보다 3배 큰값 index로 할 경우 
print(numlist[temp*3]) #90

# numlist에서 temp 값을 2로 나눴을 때의 나머지를 index로 할 경우 
print(numlist[temp%2]) #10

# numlist에서 temp 값을 5만큼 증가시킨 값을 index로 할 경우 
print(numlist[temp+5]) #80


# 4) list의 구성요소 확인
# in          list의 원소인가를 확인하는 연산자
# not   in   list의 원소가 아닌 원소를  확인하는 연산자
a = [1,2,3,4,6,12]

print(10 in numlist)
print(15 not in numlist)


#### 문제1) 파이썬반에 학생들의 이름으로 이루어진 리스트이다.
# 요구사항  '김명자'가 파이썬반 학생인지 확인해 보자

names = ['김길수','최명희','박미자','김희영']
# print('김명자' in names)

input_name =input('찾고싶은 이름을 입력하세요')

if(input_name in names):
    print(input_name+'은(는) 파이썬반 입니다')
else:
    print(input_name+'은(는) 파이썬반 아닙니다')


#### 문제2) 사고싶은 과일 리스트가 있는지 확인해보자
# 리스트가 있을 시 구매해 주셔서 감사합니다 리스트에 없으면 팔지않습니다.
# fruit_list =['사과', '귤', '포도', '망고', '바나나']

# my_fruit =input('사고싶은 과일을 입력해주세요')

# if(my_fruit in fruit_list):
#     print('리스트가 있을 시 구매해 주셔서 감사합니다')
# else:
#     print(my_fruit +'은(는) 팔지않습니다')


#### 문제2-1) 사고싶은 과일의 금액을 연동시키자!
# 사과 - 10000원, 귤 - 5000, 포도 - 15000, 망고 - 20000, 바나나- 3000
# price_list = [10000, 5000, 15000, 20000,3000]
fruit_list =['사과', '귤', '포도', '망고', '바나나']

price_list = [10000, 5000, 15000, 20000, 3000]

my_fruit =input('사고싶은 과일을 입력해주세요')

if(my_fruit in fruit_list):
    print('구매해 주셔서 감사합니다')
    if(fruit_list[0] == my_fruit):
        print('금액은'+str(price_list[0])+'원 입니다')
    elif(fruit_list[0] == my_fruit):
        print('금액은'+str(price_list[0])+'원 입니다')
    elif(fruit_list[0] == my_fruit):
        print('금액은'+str(price_list[0])+'원 입니다')
    elif(fruit_list[0] == my_fruit):
        print('금액은'+str(price_list[0])+'원 입니다')
    else(fruit_list[0] == my_fruit):
        print('금액은'+str(price_list[0])+'원 입니다')