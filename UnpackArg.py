def my_fun(**add):
    print(add)


my_fun(name="Aabid",age=22,dum=45,fun=10)

def sum(**add):
    print(add)

details = {"name":"Aabid", "age": 22}

sum(**details)


def test(**arg):
    print(arg)


def value(**arg):
    test(**arg)
    for x, z in arg.items():
        print(f"{x}: {z}")

value(name="Juned",age="22")    

h = 1
def arg(*name, **age):
    print(name)
    print(age)

arg(f"{h}:this is Tuple", "Aabid","Shaikh","Bob",name="Sunny", age=45,value=78,  num=1, name2= "Muskan / Aabid")





