#taking user inputs....
size_input = input("How big is your house is(in square feet): ")

c_meter = float(size_input)

s_meter= c_meter/10.8
print(s_meter)


h_input = input("Enter your age: ")

e_age = int(h_input)

age = e_age * 60 * 60 * 60

print(f"your age {e_age} is in seconds is:{age}")