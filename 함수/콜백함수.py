def outFunc(v1, v2) :
    def inFunc(num1, num2) :
        return num1 + num2
    return inFunc(v1, v2)

print(outFunc(10,20))

'''
def selfCall() :
    print('ha', end='')
    selfCall()
selfCall()  #무한 반복으로 에러남
'''
def selfCall(n):
    if n == 0:
        return
    print('ha', end=' ')
    selfCall(n - 1)

selfCall(5) #에러안나게 수정


def count(num) :
   if num >= 1
       print(num, end = '')
       count(num-1)
   else :
      return

count(10)
count(20)
