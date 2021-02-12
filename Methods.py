class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"hello {self.name}, is  {self.age} year old"
        

    def __init__(self, name, age):
        self.name = name
        self.age = age   

    def __repr__(self):
        return f"<Person ({self.name}, {self.age})>"    

bob = Person(name="Aabid",age=22)
bob1 = Person(name="Juned",age=23)
bob2 = Person(name="Usman",age=18)

print(bob)
print(bob1)
print(bob2)

