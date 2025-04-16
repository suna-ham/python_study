san = 'mountain'
num1 = san[0]
num1
num2 = san[4]
num3= san[6]


print(num2)

# it를 출력하기
print(num3+num2)

# 문제)  string의 indexing을 활용하여 주어진 문장으로부터 새로운 단어를 합성해 보세요
# 변수 tom은 'Tom is a good student.' string을 담고 있다
# 새로 합성할 단어는 'mood' 이다

tom = "Tom is a good student."
tom_index1 = tom[2]
tom_index2 = tom[1]
tom_index3 = tom[-10]
mood= tom_index1 + tom_index2*2 + tom_index3

print(tom_index1 + tom_index2 + tom_index3)
print(tom_index1 + tom_index2*2 + tom_index3)
print(mood)
