  ##Zadanie 1 ##

from random import randint

secret_number = randint(1, 10)
counter = 0
while counter == 0:
    try:
        user_input = input("give me number: ")
        user_number = int(user_input)
        isinstance(user_number, int)
        if user_number < secret_number:
            print("Higher!")
        elif user_number > secret_number:
            print("Lower!")
        else:
            print("Bingo!")
            counter = 1
    except ValueError:
        print("This is not a number, kiddo")

  ##Zadanie 2##

