class Person :
    name =""
    age = 0
    adress=""
    def __init__(self, *args, **kwargs) :
        if args : 
            self.name = args[0]
            self.age = args[1]
            self.adress = args[2]
        if kwargs : 
            self.name = kwargs["name"]
            self.age = kwargs["age"]
            self.adress = kwargs["adress"]
p1 = Person("Alice", 25, "서울시")
p2 = Person(name = "Bob", age=50,  adress="서울")
p3 = Person(name = "Bob", age=50, adress= "서울시")
print(p3.name, p3.age, p3.adress)