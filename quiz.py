
import random
from PIL import Image

list_of_pictures = {"448.png","squirtle.png"}
random_guess = random.choice(list_of_pictures)
def picture():
    random_guess = random.choice(list_of_pictures)
    list_of_pictures = {"448.png","squirtle.png"}
    Img=Image.open(random_guess)
    Img.show()
  


picture()
guess = input('Whos that pokemon')
if guess == random_guess:
    print('Correct')
else:
    print('Incorrect')




