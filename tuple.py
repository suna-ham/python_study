

# months = ('Jan', 'Feb', 'Dec')
# days = ('Mon', 'Tue', 'Sun')

# string_march ='March'

# type(days)

# tuple_march = tuple(string_march)
#     print(type((tuple_march))
          
                
# 튜플 수정, 삭제, 추가 안된다
# 튜플 리스트로 고쳐서 수정, 삭제, 추가

days = ('Mon', 'Tue', 'Sun')
days_list = list(days)

print(type(days_list))

# wed 추가
days_list.append('wed')
# mon 삭제

days_list.remove('Mon')

# tue를 thu 바꾸기 

days_list[1] ='Thu'

days = tuple(days_list)


n_list =list(range(1,51, 1))
# print(n_list)

ff_list = tuple(range(1,101, 5))
# print(type(ff_list))


t = ()
t_1 = (1,)
print(type(t_1))

nums = tuple(range(10))
print(nums)

tuple_t = tuple(range(10,71, 10))

sum_t=tuple_t[0]+ tuple_t[2]+ tuple_t[4]
print(sum_t)
# 튜플 읽기전용

triple = tuple(range(11))
triple =triple*3
print(triple)
print(triple[0:3])
print(triple[:5])
print(triple[10:])

# 문제1) 
# [요구사항]
# 한 중학교에서는 평소 영어, 수학, 과학, 사회 이 4가지 과목을 시험을 본다. 하지만 올해에만 수학 시험을 과제로 대체하기로 하였다.
# 이때 수학 과목만 '과제로' 대체한 리스트를 출력하는 프로그램을 작성해 보자.
# 단 원래 과목 목록은 변하지 않는다.

subject_list = ('영어', '수학', '과학', '사회')

test_list = tuple(subject_list)
work_list = list( test_list )
work_list[1] = '수학과제'
work_list =tuple(work_list)
print(work_list)


# print('테스트과목은 '+ str(test_list)+'입니다. '+ '올해만' + str(work_list) +'만 과제로 대체합니다')



# 문제2) string형과 list형으로부터 tuple형으로 바꾸어라
str_red = 'RED'

list_color = ['Red','Yellow','Orange']

list_y = list(list_color[1])

print(list_y)

