

guess_age = int(input("What age do you guess?"))
guess_gender = input("What gender?").capitalize()

dictionary_of_characters = {"Ethan":[int("14"),"Male"]}
#print (dictionary_of_characters["Ethan"][1])
hmph = dictionary_of_characters["Ethan"][0]

if guess_age == hmph:
    print('Correct Age')
else: 
    print('Incorrect Age')

if guess_gender == dictionary_of_characters["Ethan"][1]:
    print('Correct Gender')
else:
    print('INcorrect gender')

final_guess = input('Who is your final guess?')

if final_guess == "Ethan":
    print('Correct!!')
else:
    print('Incorrect answer...')