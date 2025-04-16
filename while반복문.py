# a = 1
# while (a <= 10):
#     print(a) 
#     a = a+1
# print('반복문 끝')

##실습1)
count = 1
while(count <= 5):
    print(count)
    count += 1


# 실습2) 
# 1부터 시작해 사용자가 입력한 값까지 모두 정수를 더하는 프로그램을 만들어 보자
# (1) 입력값으로 20을 넣어서 1부터 20까지의 합을 출력해 보자

n = int(input('숫자를 입력하세요 '))
step = 0
sum = 0

while( step <= n ) :
     sum += step
     step += 1
print(sum)

#### 문제1) 
# 다음은 오믈렛 재료의 일부분으로 구성된 list이다.
# omlet = ['egg','meat','onion','carrot']
# omlet에 들어 있는 모든 재료를 한번씩 출력해 주는 프로그램을 작성해 보자
omlet = ['egg','meat','onion','carrot']

for ingredient in omlet:
    print(ingredient)

print(len(omlet))