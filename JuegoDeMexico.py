#Javon Payne
#05NOV2020
#Juego de Mexico


import random

def roll_dice(player_number):
    roll = random.randrange(1,7)
    
    return roll

def print_header():
    
    print("""
                        
   
.------..------..------..------..------..------.
|M.--. ||E.--. ||X.--. ||I.--. ||C.--. ||O.--. |
| (\/) || (\/) || :/\: || (\/) || :/\: || :/\: |
| :\/: || :\/: || (__) || :\/: || :\/: || :\/: |
| '--'M|| '--'E|| '--'X|| '--'I|| '--'C|| '--'O|
`------'`------'`------'`------'`------'`------'

                              


    """)
    print("\nWelcome to the Game of Mexico!")

#Main
response = "y"

while response.lower() == "y":
    p_1 = 6
    p_2 = 6
    print_header()
    while p_1 <= 6 and p_1 > 0 and p_2 <= 6 and p_2 > 0:
        roll_1 = roll_dice(1) 
        roll_2 = roll_dice(1)
        roll_3 = roll_dice(2)
        roll_4 = roll_dice(2)
        #compare the results and modify the score.


        print("Player 1 rolled", roll_1, "and", roll_2, "for a total of", roll_1 + roll_2)
        print("Player 2 rolled", roll_3, "and", roll_4, "for a total of", roll_3 + roll_4)
        
        if roll_1 + roll_2 == roll_3 + roll_4:    #the amount of player 1 roll equals the amount of player 2 rolls
            print("It's a tie!")
        elif roll_1 + roll_2 < roll_3 + roll_4:
            #roll = random.randrange(1,6,-1)
            p_1 -= 1         
            print("Player 1 loses a life and now has", p_1, "lives")
            
        elif roll_3 + roll_4 < roll_1 + roll_2:
            #roll = random.randrange(1,6,-1)
            p_2 -= 1
            print("Player 2 loses a life and now has", p_2, "lives")
        if p_1 == 0:
            print("Player 2 wins!")
        if p_2 == 0:
            print("Player 1 wins!")
        
            
    response = input("Would you like to play again? (y/n): ")





















    
