import random

choices = ['Rock','Paper','Scissors']




running = True

def a(running):
    while running == True:
        
        player_choice = input('Rock paper scissors, what do you pick?').capitalize()
        computer_choice = random.choice(choices)
        if player_choice not in choices:
            break
        if player_choice == computer_choice:
            print('It was a tie')

        elif player_choice == 'Rock':
            if computer_choice == 'Paper':
                print ('You lose')
            elif computer_choice == 'Scissors':
                print ('You win')

        elif player_choice == 'Paper':
            if computer_choice == 'Scissors':
                print ('You lose')
            elif computer_choice == 'Rock':
                print ('You win')

        elif player_choice == 'Scissors':
            if computer_choice == 'Rock':
                print ('You lose')
            elif computer_choice == 'Paper':
                print ('You win')
        print (computer_choice)
        replay = input("Replay?").capitalize()
        if replay == "Yes":
            a(running)
        else:
            running = False
        
a(running)        
    





