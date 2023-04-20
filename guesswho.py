

guess_age = int(input("What age do you guess?"))
guess_gender = input("What gender?").capitalize()

dictionary_of_characters = {"Ethan":[int("14"),"Male","Hispanic","5'7"], "Raymond": [int("14"),"Male", "Asian", "5'9"]}
#print (dictionary_of_characters["Ethan"][1])
hmph = dictionary_of_characters["Ethan"][0]


if guess_age == hmph:
    print('Correct Age')
elif guess_age == dictionary_of_characters["Raymond"][0]:
    print('correct age')
else: 
    print('Incorrect Age')

if guess_gender == dictionary_of_characters["Ethan"][1]:
    print('Correct Gender')
elif guess_gender == dictionary_of_characters["Raymond"][1]:
    print('correct')
else:
    print('INcorrect gender')

final_guess = input('Who is your final guess?').capitalize()

if final_guess == "Ethan":
    print('Correct!!')
else:
    print('Incorrect answer...')