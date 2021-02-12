num  = 10

#user_input = input("Enter (Y/n) if you want to play: ")

while True:
    user_input = input("Enter (Y/n) if you want to paly: ")
    if user_input == "n":
       break     

    user_num = int(input("Enter the number: "))
    if user_num == num:
        print("You won")
    else :
        print("You loss")

    #user_input = input("Enter (Y/n) if you want to play: ")




