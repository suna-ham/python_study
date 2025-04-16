price={'어묵': '2000원', '떡볶이':'3000원'} 

print(price['어묵'])
print(price['떡볶이'])


L = [20, 40, 60, 80, 100] #value 리스트
T = (2, 4, 6, 8, 10) #key 튜플
lt = { }

for i in range(0, 5,1) :
    # {T[i]:L[i]}
    # print({T[i]:L[i]})
    lt[T[i]] = L[i]
print(lt)


eng = ['apple', 'banana', 'orange']
kor = ('사과', '바나나', '오렌지')

dict = { }
for i in range(len(eng)):
    dict[kor[i]] = eng[i]

print(dict)    


D = {'spring':'봄',  'summer':'여름',  'fall':'가을',  'winter':'겨울'}
print(D)
print(D['summer'])

number = {1:'one',  2:'two',  3:'three',  4:'four',  5:'five' }
print(number)
print(number[2])
print(number.values()) #number values의 리스트를 만들수있다
print(number.keys())#number keys의 리스트를 만들수있다



food = {'분식':['떡볶이','호떡'], '중식':['짜장면','탕수육']}
print(food)
print( food['중식'][0])
del food['중식']
print(food)


# 딕셔너리 만들기
d1 ={'k1':70, 'k2':70, 'k1':70}
print(d1['k1'])
d2 = {100:["a", 'b', 'c'], 200:(True, False)}

# 딕셔너리 추가하기
# ex) d1에 'k3':85
d1['k3'] =85
#ex) d2 300:'kbs'
d2[300]='kbs'
#ex) 'k2':70 삭제하기
print(d2)
del d1['k2']

# list, tulpe 딕셔너리
# {'김': 100, '박': 25, '이': 83, '최': 94} 만들어어
value_list1 = [100, 25, 83, 94]
key_tuple =('김', '박', '이', '최')

list_dict = { }
for i in range(len(value_list1)):
    list_dict[key_tuple[i]] = value_list1[i]
print(list_dict)

val_list = list_dict.values()
k_list = list_dict.keys()
print(val_list)
print(k_list)

# 문제1) 어느 커피숍에는 메뉴가 4가지 있다. Americano. Cafe latte, Green Tea latte, Mocha latte 각 메노의 가격은 2000원, 2500원, 3000원, 3500원이다. 
# 이 목록을 dictionary로 작성해 보고 Americano와 Vania latte가 있는지 없는지 확인해 보자

coffee =('Americano', 'Cafe latte', 'Green Tea latte',' Mocha latte')
price = ['2000원', '2500원', '3000원', '3500원']

cafe_menu = {}
for e in range(len(coffee)):
    cafe_menu[coffee[e]] = price[e]
    print(cafe_menu)
print('Americano' in cafe_menu.keys())
print('Vanilla latte' in cafe_menu.keys())

# 문제2) 
# [요구사항] 어는 문구점에서는 여러 문구를 판다. 연필은 200원, 펜은 800원, 지우개는 500원, 자는 300원이다.
#  이 목록은 dictionary를 이용하여 작성해보고 가격만 list로 출력해 보자

goods = ('연필', '펜', '지우개', '자')
sale = ['200원', '800원', '500원', '300원']

store_menu = {}
for f in range(len(goods)):
    store_menu














