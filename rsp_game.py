import random #random module import statements

# game option list
game_options = ["R", "P", "S"]

valid_input = True # lopp controller

user_choice = "" # users' choice holder

cpu = ""    # cpu choice holder

result = "" # Actual result holder


def game_display(choice):
    if choice == "R":
        return "Rock"
    elif choice == "P":
        return "Paper"
    elif choice == "S":
        return "Scissors"
    else:
        return False
    


while(valid_input): # repeat code after this line if variable "valid_input" doesn't change to false
        # user input
        user_choice = input('''Enter letter
        \"R\" for Rock 
        \"S\" for scissors
        \"P\" for paper: \n''').upper()

        if user_choice == "R" or user_choice == "S" or user_choice == "P":  # verify input 
            valid_input = False     # Stop loop if input is valid 
            
            cpu = random.choice(game_options) # computer's random choice
            
            print("Player (%s) \t :\t CPU (%s)" % (game_display(user_choice), game_display(cpu))) # print result
            
            # Result checker and score conditions
            if user_choice == cpu: 
                result = "Draw!!!"
                print("Result >>>>>: " + result)
                valid_input = True
                
            elif user_choice == "R" and cpu == "S":
                result = "I won!!!"
                print("Result >>>>>: " + result)   
                
            elif user_choice == "P" and cpu == "R":
                result = "I won!!!"
                print("Result >>>>>: " + result)
                
            elif user_choice == "S" and cpu == "P":
                result = "I won!!!"
                print("Result >>>>>: " + result)
                
            else:
                result = "CPU won!!!"
                print("Result >>>>>: " + result) 
        
        else:
            print("Wrong choice, please play again")  # Output if wrong input is entered before starting over
                   
        
             
        
