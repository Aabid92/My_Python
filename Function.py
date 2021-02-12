
print("Welcome to second to minute Prigram")
def user_age():
    user_age = int(input("Enter you age here: "))
    age_second = user_age * 356 * 24 * 60 * 60
    print(f"You age in Second is: {age_second}")


def user_age1():
    user_age = int(input("Enter you age here: "))
    age_second = user_age * 356 * 24 * 60 
    print(f"You age in Minimute is: {age_second}")
 



user_age()
user_age1()

print("Thnak you")

# dost = ["A","B","C"]

# def dost():
#     dost_name = input("Enter your dost name: ")
#     do = dost1 + [dost_name]
# dost()    
dost1=["Aabid1","Juned"]
def dost():
    dost1.append("Aabid")
    dost1.remove("Aabid1")

dost()
print(dost1)

add_number = []
def add_name():
    add_number.append("Aabid")


add_name()
add_name()
print(add_number)



def my_function(x , y):
  return(x * y)
    
    
print(my_function(5, 7))

def name(name, sername):
      print(f"name is {name} and Sername is {sername}")

name(name= "Aabid", sername= "Shaikh")



def divide(divider, num):
    if num != 0:
        print(divider / num)      # we can use return too
    else:
        print("Chutiya hai tu")   # we can use return too here


divide(15 , 48) #  * 5 this will only work with (return) 

user_input = int (input("Which table do you want: "))

print("The table of -> ",user_input)

for x in range(1, 11): 
    print(user_input, "X",x, "=", x * user_input)

stop = input("Press Enter to Exit...")
