#1~10까지 합을 구하기
sum = 0
for a in range(1,11,1):
  sum = sum + a
print(sum)  


#2,4,6, 8,10까지 합을 구하기

sum1 = 0
for a1 in range(2,11,2):
  sum1 = sum1 +a1
print(sum1) 

#1~20까지 홀수의 합 구하기

sum2 =0
for a2 in range(1,21,2):
  sum2 =sum2 + a2
print(sum2)

print('★'*5)
print('★'*4)
print('★'*3)
print('★'*2)
print('★'*1)

for i in range(0,4):
    print('★'*5)

for i in range(0,5):
    print('★'*(i+1))

for i in range(0,5):
    print('★'*(5-i))

