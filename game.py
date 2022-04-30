#rock paper scissors program

while(True):

    player_1 = input("player 1: ")
    player_2 = input("player 2: ")
    
    #Rock beats scissors
    #Scissors beats paper
    #Paper beats rock
    #if player 1 plays 
    #rock 
    
    d = {
        "rock" : "scissors",
        "scissors" : "paper",
        "paper" : "rock"
    }
    
    if(player_1 != player_2):
        winner = "player 2 wins" if d.get(player_2) == player_1 else "player 1 wins"
    else:
        print("player 1 and 2 played the same piece TRY AGAIN!!! ")
        
        
    print(winner)
    c = input("#play again(y/n): ")
    
    if(c == 'n'):
        break
        
        
