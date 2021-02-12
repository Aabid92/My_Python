x = 5, 11
y, z = x

print(y,z)

student = {"Aabid": 100,  "Juned": 80, "Usman": 55}

#print(list(student.items()))

for v,att in student.items():
    print(v,att)
    
#""'for atten , attendance in student.items():
    #print(f"{atten}:{attendance}%")
person = ("Bob,",42, "CA")

name,_, Pro = person

print(name,Pro)

*head, tail = [1,2,3,4,5,67,8]

print(head)
print(tail)
