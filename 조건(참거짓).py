# 사이트에 회원을 가입하기 위해서는 id와 password를 입력해야한다. 문자열의 길이가 10자를 넘지 않는다는 제약 사항이 있다. id길이가 10을 넘으면 '회원가입 실패 : id가 10글자를 넘었습니다'라고 메시지 출력하고
# password길이가 10을 넘으면 '회원가입 실패 : password가 10글자를 넘었습니다'라고 메시지를 출력하는 프로그램
# 모두 아니면 '회원가입 성공!' 의 메시지를 출력하는 프로그램


# input_id = input('id입력')
# input_pw = input('password입력')

# if(len(input_id) < 10):
#     print('회원가입 실페 : 10자리 이상입력 요망')
# elif(len(input_pw) < 10):
#     print("비밀번호 실패")
# else:
#     print('회원가입성공')


# 문제1) 0이 아닌 두 정수를 곱하는 경우 양수*양수  또는 음수 * 음수 일때 양수가 되고, 
# 양수 * 음수 일때는 음수가 된다.
# 두수를 입력받아서 양수인지 음수인지를 예상하는 프로그램 작성하여라

# num1 = int(input('첫번째 숫자를 입력하시오'))
# num2 = int(input('두번째 숫자를 입력하시오'))
# double = num1*num2
# if(double < 0):
#     print(str(double)+ " 음수입니다.")
# else:
#     double >= 0
#     print(str(double)+" 양수입니다.")

# 문제1) TV 채널의 구성은 SBS - 6  KBS - 7 MBC = 11 EBS - 13 
# 번호를 입력으로 받아 채널을 출력하는 프로그램을 작성하세요

chanel_num = int(input("채널번호를 입력하세요"))
if ( chanel_num == 6 ):
    print('SBS입니다')
elif(chanel_num == 7):
    print('KBS입니다')
elif(chanel_num == 11):
    print('MBC입니다')
elif(chanel_num == 13):
    print('EBS입니다')
else:
    print('없는 채널입니다')