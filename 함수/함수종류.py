#함수생성(함수정의)
'''
def 함수이름(매개변수1, 매개변수2, ...):
    # 함수가 수행할 코드
    return 반환값  # 선택사항, 값을 반환할 때 사용
'''
def plus(v1, v2):
    result = 0
    result = v1 + v2
    return result

hap = plus(10, 20) 
print(hap)
'''
**숫자3개를 함수로 보내서 큰 수 리턴받기
 - 1단계 함수만들기
 - 2단계 함수호출

def max_fun(n1, n2, n3):
    

    return max_value

max_v = max_fun(10, 20, 30)
'''

# 문자 2개 함수 보내서 합을 출력

def theham(su1, su2):
    plus = 0
    plus = su1 + su2
    return(plus)

my1 = theham(2,780)
print(my1)

def mun(nn1, nn2, txt1):
    if( txt1 == '+'):
        r = nn1 + nn2
    elif( txt1 == '-'):
        r = nn1 - nn2
    elif(txt1 == '*'):
        r = nn1 * nn2
    elif(txt1 == '/'):
        r = nn1 / nn2

    return (r)

my2 = mun(1, 3, '*')
print(my2)

def calc_f():
    global n3 #w전역변수처리
    n3=100
    print(f'{n1}{o1}{n2}')
n1=10
n2=20
o1='+'
calc_f(n3)


res = 0 
var1, var2, oper = 0, 0, ""

# 커피 자판기를 프로그래밍해보자
## 전역변수
coffee = 0
## 지역변수
def coffee_machine(button):
    print()
    print('#1.(자동으로 )뜨거운 물을 준비한다')
    print('#1.(자동으로 )종이컵을 준비한다')

    if button == 1:
        print('#3. (자동으로)보통커피를 탄다')
    elif button == 2:
        print('#3. (자동으로)설탕커피를 탄다')
    elif button == 3:
        print('#3. (자동으로)블랙커피를 탄다')
    else:
        print('자동으로 아무거나 탄다 ')
    print('#4.(자동으로 )물을 붓는다')
    print('#5.(자동으로 )스푼으로  젓는다')
    print()

coffee 
