# Advance set Operation............... 

myFriends = {"Suraj", "Muskan", "Vishal", "Tejas"}

yourFriends = {"Suraj", "Vishal", "Tejas"}

comman = myFriends.intersection(yourFriends)  #intersection is give common value or items in both set

uni1 = yourFriends.union(myFriends)           #union is unite the items of set toghater 

uni2 = myFriends.union(yourFriends)

print(uni2)

print(uni1)

print(comman)

art = {"A","B","C","D"}

commerce = {"A","C","V","E"}

both = art.intersection(commerce)

diff = commerce.difference(art)
diffa = art.difference(commerce)
uni = art.union(commerce)

print(uni)

print(f"The Student who are doing arts and Commerce both at same time is {both}")

print(f"The student who only doing Commerce{diff}")

print(f"The student who only doing arts: {diffa}")

print("\t\t......................Thank You....................")
