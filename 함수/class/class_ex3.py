class Dog:
    c_var ="클래스변수"
    c_i_var = 100

    def __init__(self):
        self.in_var ="인스턴스 변수"
        self.in_i = 200

myDog = Dog()
print(myDog.c_var)
print(myDog.c_i_var, myDog.in_var )
print(Dog.c_var, Dog.c_i_var)
print(Dog.in_var, Dog.in_i)

