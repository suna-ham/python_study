# while(True) :
#      n   =  int(input('enter the number :'))
#      if  n == 0 :
#         print("EXIT")
#         break;
#      elif  n%2  == 0
#         print(n, 'is even number')
#      else  :
#         print(n,'is odd number')

# while(True) :
#     n = int(input('숫자를 입력하세요'))
#     print(n)
#     if n == 0:
#         print('멈추세요')
#         break
#     print(n)



# 문자를 입

i = 0
sum = 0

while sum <= 1000:
    i = i + 1
    sum = sum + i 
    print(f"현재 합: {sum}, 현재 i: {i}")
    
    # 'a'를 입력받으면 반복문 종료
    user_input = input('중단하려면 "a"를 입력하세요: ')
    if user_input == 'a':
        print('중단되었습니다')
        break

print(f"반복문 종료 시 i 값: {i}")