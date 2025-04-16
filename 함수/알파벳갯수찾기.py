# 문제10 사용자 함수를 이용하여 영어문장에 있는 알파벳의 개수를 카운트하는 프로그램을 작성하시오

# 실행결과
# 영어문장을 입력하세요 I am a student
# 알파벳 하나를 입력하세요 a
# I am a student에 포함된 a의 개수는 2개입니다

def cnt(subject, single_voca):
    cnt = 0
    for i in subject:
        if (single_voca == i ):
            cnt = cnt+ 1
    return cnt
subject = input('영어 문장을 입력하세요')
single_voca = input('갯수를 찾을 알파벳을 입력하세요')

cnt(subject, single_voca)
result = cnt(subject, single_voca)
print(subject, '에 포함된', single_voca, '의 갯수는', str(result),'개 입니다.')