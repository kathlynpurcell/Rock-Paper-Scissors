import numpy as np
import time

yn=input("Would you like to play (yes or no)?  ")

while (yn=="yes") or (yn =="Yes") or (yn == 'yea') or (yn == 'ok'):
    print("Rock")
    time.sleep(0.5)
    print('paper')
    time.sleep(0.5)
    print('scissor')
    time.sleep(0.5)
    print("shoot!")
    phand=input("Pick rock paper or scissors: ")
    hand=np.random.randint(1,3)
          

    if hand == 1:
        hand = 'rock'
    elif hand == 2:
        hand = 'paper'
    else:
        hand == 'scissors'
        
    print("\n You chose: ", phand)
    print("The computer chose: ", hand)
    
    
    if (hand == 'rock') and (phand=='paper'):
        print("Player wins")
    elif (hand == 'rock') and (phand =='scissors'):
        print("Computer wins")
    elif (hand == 'paper') and (phand =='scissors'):
        print("Computer Wins")
    elif (hand == 'paper') and (phand == 'rock'):
        print("Player wins")
    elif (hand =='scissors') and (phand == 'paper'):
        print("Computer wins")
    elif (hand == 'scissors') and (phand == 'rock'):
        print("Player Wins")
    elif hand == phand:
        print("Its a draw")
    else:
        print("Wrong input, you lose")
        

    yn=input("\n\n Would you like to play again?  ")

