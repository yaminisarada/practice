def correct_value():
    while True:
        try:
            user_input = int(input("Enter the integer: "))
            print("You entered {}".format(user_input))
            break
        except(ValueError):
            print("try again")
            
        
correct_value()
