name = "Aabid"

print(f"hello,{name}")

name = "Juned"

print(f"hello,{name}")

name = "someone"

greeting = "hello,{}"  

with_name = greeting.format(name)
with_name1 = greeting.format("Aabid")
print(with_name1)

print(with_name)

long_string = "hello , {}. Welcome to ,{}."

format_string = long_string.format("Aabid" ,"Hell")
print(format_string)


