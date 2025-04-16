# list_name = ['e', 'a', 'q', 'f', 'd', '1', 'A', 'p']
# list_name.sort()
# print(list_name)
# list_num = [10, -20, 55, 200, 0]
# list_num.sort()
# print(list_num)

# ==============================================================
# 종합문제
# =============================================================
# 문제1)  요구사항 
# winner=['박민아', '정민호', '김철수', '이영희', '손수정']
# 위의 list는 어떤 공모전의 수상자 명단이다.
# 1) 정수지가 수상했는지 확인하라.
# 2) 김철수가 수상하지 못했는지 확인하라.
# 3) 박민아가 수상했는지 확인하라.
# 4) 전은진이 수상하지 못했는지 확인하라.

# winner=['박민아', '정민호', '김철수', '이영희', '손수정']

# check = input('확인할 수상자 이름을 입력하세요')

# check in winner
# if (check in winner):
#     print(check+"은 수상했습니다")
# else:
#     print(check+'수상하지 못했습니다')


# print(10 in numlist)
# print(15 not in numlist)


# 문제2) 수학 시험을 5회 응시한 후 점수를 각각 90점, 75점, 30점, 100점, 85점을 받았다. 
# 이 점수들을 각각 score라는 list 안에 저장했고, list의 성격을 이용해 평균을 구해보자. 

# rank1 = int(input('점수1를 입력하세요'))
# rank2 = int(input('점수2를 입력하세요'))
# rank3 = int(input('점수3를 입력하세요'))
# rank4 = int(input('점수4를 입력하세요'))
# rank5 = int(input('점수5를 입력하세요'))

# score = [rank1, rank2, rank3, rank4, rank5]

# print((score[0]+score[1]+score[2]+score[3]+score[4])/5)


# score = []
# a = int(input( "점수?"))
# score.append( a )
# a = int(input( "점수?"))
# score.append( a )
# a = int(input( "점수?"))
# score.append( a )
# a = int(input( "점수?"))
# score.append( a )
# a = int(input( "점수?"))
# score.append( a )
# print( score )
# sum = score[0] + score[1] + score[2] + score[3] + score[4]
# avg = sum / len(score)
# print("평균 :" + str( avg ))


# 문제3) 0부터 5까지의 숫자 중 하나를 골라 입력하면 오늘의 운세를 알려는 준 포춘쿠키와 비슷한 프로그램이다
# list인 goodsay안에는 happy, love, sad, hot, angry, fortunate가 들어 있다. 
# 숫자를 골라 입력하면 오늘의 운세를 알려주는 프로그램을 작성하여라

# 문제해결 알고리즘
# num->0~5가지의 숫자를 하나만 입력 받아 저장한다.
# goodsay[num]하여 출력한다.

# num = [0, 1, 2, 3, 4, 5]
num = int(input('0~5 중에 숫자를 입력하시오'))
word = ['happy', 'love', 'sad', 'hot', 'angry', 'fortunate']

if 0 <= num <=5:
    print('goodsay '+ word[num])
else: