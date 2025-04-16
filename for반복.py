# 문제7) for문 문제입니다 주식상황으로 예시시
ohlc = [["open", "high", "low", "close"], [100, 110, 70, 100], [200, 210, 180, 190], [300, 310, 300, 310]] 
# close값 100, 190, 310을 출력해 보세요.
# 에서
print(ohlc[1][3], ohlc[2][3], ohlc[3][3])


for e in ohlc[1:]:
    print(e[3])



list_0_90 =(list (range(0,9,18)))

# alpha = 'abcde'
# for i in alpha(:):
#     if  

# text = "abcde"[:]
# for i, char in enumerate(text[:], start=1):
#     print(f"{char}는 {i}번째입니다")


# text = "abcde"[:]

# for i in range(len(text)):
#     print(f"{text[i]}는 {i + 1}번째입니다")

# str = 'abcde'
# for i in range(len(str)):
#     i1 = i+1
#     print(f'{i1}번째 알파벳 {str[i]}')


# n=  int(input("숫자는?"))
# f = 1
# for i in range( n, 0, -1):
#    f = f*i 
# print( f'{n}! = {f}' )


# 문제1) mix_list = ['apple', 5, 'banana', 'grape', 3, 8, 6,'melon']
# mix_list의 각 element의 형이 string형인지, int형인지 판별해 출력하기

# mix_list = ['apple', 5, 'banana', 'grape', 3, 8, 6,'melon']

# type_list = type(mix_list[i])

# for i in range(len(mix_list)):
#     type_list = type(mix_list[i])
#     # print(type_list)
#     # print( mix_list[i] ,type(mix_list[i]))

# mix_list2 = mix_list[i] ,type(mix_list[i])
# list_type = type(mix_list[i])
# print(mix_list2)
# num_list = []
# str_list = []

# for i in list_type:
#     if isinstance(list_type, int):
#         num_list[]
#     elif isinstance(list_type, str):

mix_list = ['apple', 5, 'banana', 'grape', 3, 8, 6,'melon']
num_list = []
str_list = [] 
for i in range( len(mix_list) ) : 
  if( type(mix_list[i]) == str):
     str_list.append( mix_list[i])
  elif( type(mix_list[i]) == int):  
     num_list.append( mix_list[i] )  
print( "숫자리스트 : ", num_list )
print( "문자리스트 : ", str_list )