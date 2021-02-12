print( (lambda x , y:x + y)(2, 78) )


#print (add (4 , 5))


def double(x):
    return x * 2

l = [1,2,3,4]

doubled = [double(v) for v in l]
doubled = list (map(double , l))

def sum( *name, **age):
    print(name)
    print(age)

sum(name="Aabid", age=22, H=5.6,)

def loop(lop):
    print(lop)

    f = [45,69,78,56,26,59,48,13,56,25]
    for x in  f:
     print(x)
           

loop(lop="Aabid")

user_input = input("Press Enter to exit....")
