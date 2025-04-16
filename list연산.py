# 5. list형의 연산

# 1) list형 간의 연산자 : "+"
# list형들 사이에 "+"의 의미는 두 list형들을 합하여 새로은 list형을 생성하는 것이다.

int_num_a=[0,1,2,3]
int_num_b=[4,5,6]
int_num_ab = int_num_a + int_num_b
print(int_num_ab)

int_num_a3 = int_num_a*3
print(int_num_a3)


list_odd = [1,3,5,7,9]
list_even = [2,4,6,8,10]
list_odd[-3]

list_even[1+3]

list_plus = list_odd + list_even

print(list_plus)
list_odd2 = list_odd*2
print(list_odd2)
print(list_odd[0:3])
print(list_even[:])
print(list_even[4:])