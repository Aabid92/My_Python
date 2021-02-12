
number = 7
user_input = input("Enter 'y' if you want to play: ").lower()

if user_input in ("'y' 'Y' 'Yes' 'yes' YES"):
    user_number = int(input("Gusee the Number: "))
    
    if user_number == number:
        print("You Won.....") 
    
    elif number - user_number in (1,-1):
    #elif abs (number - user_number) == 1:    
            print("You were off by 'One'")
            
    else:
          print("You loss------")
