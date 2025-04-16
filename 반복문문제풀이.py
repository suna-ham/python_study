'''
# 문제2)  1이상의 정수를 입력하면 그 수의 약수를 출력해주는 프로그램이다.  for문을 이용해 작성해보자. 
mynum = 4 #nt(input('1이상의 정수를 입력하시오 >>'))
divisor = []
for i in range(1, mynum+1, 1):
    if mynum%i == 0:
       divisor.append(i)
print(divisor)

# 문제3) 리스트를 원소로 갖는 리스트의 각 원소들의 합을 구하는 프로그램을 while문을 이용하여 작성해보자.
# a = [(1, 3), (3, 5), (7, 9), (13, 15)]
a = [(1, 3), (3, 5), (7, 9), (13, 15)]
plus_num = []
i = 0 
while i < len(a):
  el_sum = a[i][0] + a[i][1]
  #print(a[i][0] + a[i][1] )
  plus_num.append(el_sum)  
  i = i+1 #i += 1
  print(plus_num)

a = [(1, 3), (3, 5), (7, 9), (13, 15)]
plus_num = []
i = 0 
while i < len(a):
  el_sum = a[i][0] + a[i][1]
  #print(a[i][0] + a[i][1] )
  plus_num.append(el_sum)  
  i = i+1 #i += 1
  print(plus_num)


#문제3 -1  pack을 이용해서 작성해보자

a = [(1,3),(5,7),(9,11),(13,15)]
i = 0

while( i < len(a) ) :
   (n1 , n2)=a[i]  # 튜플로 감싸있는 부분을 unpack
   print( n1 + n2 )
   i += 1


# 문제4) 다음의 요구사항에 따라 프로그램을 작성하시오.
# I 요구사항 I
# 시험을 치른 후, 맞은 개수를 알려주는 프로그램이다. 사용자의 이름과 문제의 개수를
# 입력하고, 문제를 맞혔는지 아닌지를 입력하면 맞은 개수를 출력해준다.
# for문을 이용해서 프로그램을 작성해보자.
name = (input('이름은:'))
q_count= int(input('문제갯수'))
for i in range(q_count):
    #range(q_count)는 range(0, q_count1, 1)을 생략한 표현임
    yn = input(i+1, '번 문제를 해결했나요?(y/n)')
    if ( yn == 'y'):
        q_count += 1
print(name, "학생 총 ", q_count, "문제를 해결했습니다")

'''
# 문제5) 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의 하세요.
# 시가	    종가
# 100   	80
# 200	    210
# 300	    330
market = ['시가', 100, 200, 300]
close = ['종가', 80, 210, 330]
stock = [market, close]

print(stock)


apart = [ [101, 102], [201, 202], [301, 302] ]
for ap in apart :
    for a in ap: # [101, 102]
       print( str(a) + "호", end=" " )

#리스트에 담는건


# apart = [ [101, 102], [201, 202], [301, 302] ]
# ap_list = []
# for ap in apart :
#     for a in ap: # [101, 102]
#        ap_list.append( str(a) + "호" )


apart = [ [101, 102], [201, 202], [301, 302] ]
for ap in apart[ ::-1 ] :
    for a in ap[::-1]: 
       print( str(a) + "호", end=" " )
    print() 