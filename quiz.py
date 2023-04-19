
import random
from PIL import Image


def picture():
   
    list_of_pictures = ["448.png", "squirtle.png"]
    random_guess = random.choice(list_of_pictures)
    Img=Image.open(random_guess)
    Img.show()








