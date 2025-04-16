# 문제9) 사용자 함수를 정의하여 킬러미터를 마일로 환산하는 프로그램을 작성하시오
# 힌트 환산 수식 
# 마일 = 킬로미터 X 0.621371
# 실행결과
# 킬로미터를 입력하세요 30
# 30킬로미터는 18.64마일입니다
def out_mile(input_km):
    mile = input_km * 0.621371
    return mile

input_km = float(input('킬로미터를 입력하세요: '))
result = out_mile(input_km)
print(f'{input_km}킬로미터는 {result:.2f}마일입니다.')