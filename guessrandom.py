from operator import truediv
import random

r = random.randint(0,100)

while True:
    x = int (input("enter the number you guess:"))
    if x == r:
        print('you got it!!!')
        break
    elif x < r:
        print('higher')
    else:
        print('lower')
    