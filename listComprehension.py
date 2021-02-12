#dost = ["Aabid", "Shaikh", "Naima","Suraj","Vishal","Abdul"]

v = [1,2,3]

k = [x * 5 for x in v]

print(k)

dost = ["Aabid", "Shaikh", "Naima","Suraj","Vishal","Abdul"]

starts_s = [friend for friend in dost if friend.startswith("S")]

#for friend in dost:
 #   if friend.startswith("S"):
  #      starts_s.append(friend)
print(starts_s)
print(dost != starts_s)

print("friend: ", id(dost), id(starts_s))


w = ["Aabid", "Damm","Sunny","Abc","Avv"]

with_a = [f for f in w if f.startswith("A")]
  
print(with_a)




