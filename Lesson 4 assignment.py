import random

def get_user_weapon():
    print("SELECT YOUR WEAPON " "1-3")
    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")
    

    
    user_choice = int(input("Enter your weapon: (1-3): "))
    return user_choice

def get_opponent_weapon():
    opponent_choice = random.randrange(1, 4)  
    return opponent_choice

def determine_winner(user_weapon, opponent_weapon):
    if user_weapon == opponent_weapon:
        print("It's a tie for both!")
    
    elif (user_weapon == 1 and opponent_weapon == 3):
        print("You win Rock crushes scissors")
        
    
    elif(user_weapon == 2 and opponent_weapon == 1):
        print("You win Paper covers rock")
      
    
    elif(user_weapon == 3 and opponent_weapon == 2):
            print("You win Scissors cuts paper")
            
    else:
        print("Sorry you lose buddy!")

def main():
    continue_playing = True
    
    
    while continue_playing:
        user_weapon = get_user_weapon()
        opponent_weapon = get_opponent_weapon()

        determine_winner(user_weapon, opponent_weapon)

        play_again = input("Would you like to play again? (y/n): ").lower()
        continue_playing = (play_again == "y")

    print("Completed by: Armando Gaona")

#calling main with the if __name__method
if __name__ == "__main__":
    
    main()
