class ClassTest:
    def isinstance_method(self):
        print (f"We are calling instance methold of {self}")

    @classmethod
    def class_method(cls, name):
        print(f"We are calling classmethod of {cls}")   
        cls.value = name

    @staticmethod
    def static_method():
        print(f"We are calling Static Method")

ClassTest.class_method(name=1)

test = ClassTest.class_method(name="Aabid")
ClassTest.static_method()
ClassTest.isinstance_method(test)
ClassTest.class_method(test)








