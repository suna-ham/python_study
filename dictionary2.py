# while( True ) :
#   in_date = input('알고 싶은 날짜는? ') # '09/06'
#   if( in_date in date ):
#     print("종가는 ", close_table[ in_date ], '원 입니다' )
#   elif( in_date == '99/99'):
#     print("프로그램종료")
#     break 
#   else :
#     print("데이터가 없습니다") 

mugu ={'연필': 200, '펜':800, '지우개':500, '자':300 }
mugu_keys = list(mugu.keys())
mugu_vals = list(mugu.values())
  # mugu_vals = 
print(mugu_vals)
# 문제4) 영수의 집에 과일이 아래 표와 같이 있을 때, 5개 이하인 과일은 5개가 되도록 사려고 할 때,
#  사야 할 과일과 그에 드는 각각의 비용과 총비용을 출력하는 프로그램을 작성하라.
# [문제해결]
# 배 = [2000,3]
# 사과 = [1500,5]
# 딸기 = [1800, 2]
# 참외 = [2300, 5]
# 문제4
d1 = {'배':[2000,3], '사과':[1500,5], '딸기':[1800,2], '참외':[2300,5]}
total = 0

if( d1['배'][1] <= 5 ):
     p1 = 5-d1['배'][1]
     price1 = p1 * d1['배'][0]
     total = total + price1
if( d1['사과'][1] <= 5 ):
     p2 = 5-d1['사과'][1]
     price2 = p2 * d1['사과'][0]
     total = total + price2
if( d1['딸기'][1] <= 5 ):
     p3 = 5-d1['딸기'][1] 
     price3 = p3 * d1['딸기'][0]
     total = total + price3
if( d1['참외'][1] <= 5 ):
     p4 = 5-d1['참외'][1] 
     price4 = p4 * d1['참외'][0]  
     total = total + price4 
if( p1 != 0 ):
     print( '배',  str(p1) +'개' , str(price1)+ '원' )
if( p2 != 0 ):
     print( '사과', str(p2) +'개' , str(price2)+ '원' )
if( p3 != 0 ):
     print( '딸기', str(p3) +'개' , str(price3)+ '원' )
if( p4 != 0 ):
     print( '참외', str(p4) +'개' , str(price4)+ '원' )               
print("총 비용 ", total )


# 위의 코드는 비효율적이다 코드를 항목이 늘어나도 사용가능하도록
# 확장시켜 정리해보자자
d1 = {'배':[2000,3], '사과':[1500,5], '딸기':[1800,2], '참외':[2300,5]}
d1_keys_list = list( d1.keys() ) #['배','사과'...]
total = 0
for key in d1_keys_list :
     if(5-d1[key][1] != 0):
        print( key, 5-d1[key][1], (5-d1[key][1]) * d1[key][0] )
        total += (5-d1[key][1]) * d1[key][0]
print( "총 비용은", total )  
    


#  문제5] 아래의 표에서, 아이스크림 이름을 키 값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.
# 이름	가격	재고
# 메로나	300	20
# 비비빅	400	3
# 죠스바	250	100

# inventory ={'메로나' : [300,20], '비비빅'  : [400,3], '죠스바': [250,100] }

# 문제6] 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 
# 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.

# 통화명	환율
# 달러	  1167
# 엔	   1.096
# 유로	  1268
# 위안	   171


money = {'달러':[100, 1167],'엔':[1000, 1.096], '유로': [13, 1268], '위안':[100, 171]}
nation_k =  list[money.keys()]
global_v = list[money.values()]
# global_v2 = set(global_v)
print([global_v][0])
# excha = 0
# for i  in nation_k:
#     if (global_v2[1]*global_v2[0]):
#         print(str(excha)+' 원')






str = "Welcome Python World"

str.split( )

print(str.split( ))



m_ex={ '달러':1167, '엔':1.096, '유로':1268, '위안':171}
keys_list = list(m_ex.keys())
while( True ) :
    a=input("환전할 금액과 단위입력(예: 100 달러)")
    money, unit = a.split(' ')
    print( money, unit  )
    money = int(money)
    if( unit == '종료'):
        break
    for key in keys_list:
        if( key == unit ):
            print( money * m_ex[ key ], '원')


















