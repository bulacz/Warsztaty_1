from random import sample


def user_numbers():
    user_number_array = []
    user_number_index = 0
    while user_number_index < 6:
        try:
            user_input = input("Give me number: ")
            user_number = int(user_input)
            isinstance(user_number, int)
            if (user_number >= 1) and (user_number <= 49):
                if user_number in user_number_array:
                    print("Number already typed")
                else:
                    user_number_array.append(user_number)
                    user_number_index += 1
            else:
                print("Your number is out of range. Must bt <1,48>")
        except ValueError:
            print("This is not a number, kiddo")
    return user_number_array


 #losowanie liczb w totka
winning_number_array = sample(range(1, 49), 6)

 #pobieranie danych od użytkownika
user_numbers = user_numbers()

 #sprawdzenie czy user trafił
correct_number = 0
for lucky_number in user_numbers:
    if lucky_number in winning_number_array:
        correct_number += 1
if correct_number >= 3:
    print("Jackpot!")
else:
    print("Sorry!")