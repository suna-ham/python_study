# # 1~30
# for num in range(1,11):
#     print(num, end='')

# #문구점 상품리스트 :펜, 지우개, 샤프, 자

# shop_list = ['펜','지우개','샤프','자'] 
# while( True ):
#   buy = input('사고 싶은 상품은?(종료 no)')
#   if( buy in  shop_list ):
#      print( buy + " 여기 있습니다")
#   elif( buy == 'no'):
#      break
#   else:
#      print( buy + "는(가) 없습니다")


# 학생이름은?(종료 exit) 홍길동
# 홍길동은 학생명단에 없습니다
# 학생1은 우리반 학생입니다
# 종료시 수고 많이 하셨습니다 우리반 학생은 3명입니다.
# student_list =['학생1','학생2','학생3']
# while(True):
#     man = input('학생이름은?(종료 exit)')
#     if(man in student_list):
#       print(man+' 우리반 학생입니다')
#     elif(man == "exit"):  
#         print('종료시 수고 많이 하셨습니다.'+  str(len(student_list)) +'명 입니다.')
#         break
        
#     else:
#         print(man+' 우리반 학생입니다')


# student_list = ['학생1', '학생2', '학생3']

# while(True):
#     man = input('학생이름은?(종료 exit): ')
    
#     if(man in student_list):
#         print(man + ' 우리반 학생입니다')
#     elif(man == "exit"):
#         print('종료시 수고 많이 하셨습니다. 총 ' + str(len(student_list)) + '명 입니다.')
#         break
#     else:
#         print(man + ' 우리반 학생이 아닙니다')

# 반찬가게 관리 프로그램
food_list = ['김치','멸치볶음']
while(True):
   print()
   print( '1.추가 2. 삭제 3. 전체목록 9. 종료')
   menu = int(input('메뉴를 선택하기 '))
   if( menu == 1) :
      food_append=input('추가하고 싶은 반찬종류는? ')
      if( food_append not in  food_list):
         food_list.append( food_append  )
      else: 
         print("이미 목록있는 반찬입니다")   
   elif( menu == 2 ):
      food_remove = input('삭제하려는 반찬명은?')
      if( food_remove in food_list ):
         food_list.remove( food_remove )
      else:
         print( food_remove + " 반찬은 목록에 없어요")   
   elif( menu == 3) :
      for food in food_list :
         print( food, end=" ")
   elif( menu == 9 ) :
      break      

# 리스트 원소추가 append

# # 리스트 원소를 삭제하기 리스트명.remove(원소값)
# a_list = [1,2,3]
# a_list.remove(1)
# print(a_list)


# a_list = ['사과', '배', '복숭']
# a_list.remove('복숭')
# print(a_list)


# # 인덱스번호로 지우기 del b_list[인덱스번호]
# b_list = ['사과', '배', '복숭']
# del b_list[0]  # Delete the element at index 0 (which is '사과')
# print(b_list)