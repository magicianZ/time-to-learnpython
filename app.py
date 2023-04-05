import random



def find():
    list = [1,2,3,4,5,6,7,8,9,10]
    guess = random.choice(list)
    user_guess = input('Guess a number between 1 and 10')
#    while user_guess == guess:
#        print('Correct')
        
    while user_guess == guess:
        print('correct')
    if user_guess != guess:
        for x in range(5):
            user_guess = input('Try again')
    print(guess)

    
   


find()