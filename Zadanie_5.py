from random import randint
"""
Symulacja rzutu kośćmi, według rozkodowanego stringa będącego inputem funkcji. Kod stringa: xDy+z, gdzie: 
    x - liczba rzutów
    y - rodzaj kości (D3, D4, D6, D8, D10, D20, D100)
    z - modyfikato wyniku
"""

  # rozkodowanie stringa będącego wejściem od użytkownika
def dice_input():  # założenie kodu w postaci xDy+z np 10D6+10. Rezultatem jest tablica [x, D, y, +, z]
    dice_code = input("Podaj kod działania: ").upper()  # pobiera string i zamienia małe litery w wielkie 12d15 -> 12D15

    if "+" in dice_code:  # jeśli w kodzie występuje modyfikator (+)
        how_many_dices = list(str.partition(dice_code, "D"))
        '''
        Parsowanie stringa do postaci listy [ 10, D, [6+10]. Domyślnie str.partition tworzy krotkę. 
        Efektem jest tabela, na ostatnim miejscu mająca kolejną tabelę - złożoną z elementów stringa po D
        '''
        for element in list(str.partition(how_many_dices[2], "+")):  # dodanie elementów wewnętrznej tablicy do tablicy zewnętrznej
            how_many_dices.append(element)  # [10, D, [6+10], 6, +, 10]
        how_many_dices.pop(2)  # zrzucenie wewnętrznej tablicy - efektem jest tablica w której kolejnymi elementami są kolejne części stringa wejściowego [10, D, 6, +, 10]
        return how_many_dices
        '''
        Poniżej to samo, tylko dla stringa z minusem
        '''
    elif "-" in dice_code:
        how_many_dices = list(str.partition(dice_code, "D"))
        for element in list(str.partition(how_many_dices[2], "-")):
            how_many_dices.append(element)
        how_many_dices.pop(2)
        return how_many_dices
        '''
        JEśli w stringu wejściowym nie było ani plusa, ani minusa
        '''
    else:  # Kod kostki podany bez modyfikatora
        how_many_dices = str.partition(dice_code, "D")
        return how_many_dices  # (10, D, 6)

'''
Funkcja obliczająca wynik kodu według wskazań tablicy stworzonej ze stringa z danymi wejściowymi
'''

def dice_operation(dice_array):
    accepted_dices = (3, 4, 6, 8, 10, 20, 100)
    try:
        if int(dice_array[2]) in accepted_dices:  # kontrola warunku właściwej kostki - musi mieć odpowiednią ilość ścianek
            if not dice_array[0] == "":  # jeśli pierwszy znak stringa wejściowego nie był pusty (czyli, jeśli istnieje mnożnik rzutów)
                if dice_array[-2] == "+":  # jeśli istnieje modyfikator "+"
                    result_number = int(dice_array[0]) * randint(1, int(dice_array[2])) + int(dice_array[-1])  # działania na kolejnych elementach tablicy - stringa wejściowego
                    return result_number
                elif dice_array[-2] == "-":  # jeśli istnieje modyfikator ujemny
                    result_number = int(dice_array[0]) * randint(1, int(dice_array[2])) - int(dice_array[-1])
                    return result_number
                else:  # jeśli istnieje mnożnik rzutów, ale nie ma modyfikatora + - do wyniku
                    result_number = int(dice_array[0]) * randint(1, int(dice_array[2]))
                    return result_number
            elif dice_array[0] == "":  # jeśli pierwszy wyraz stringu nei był liczbą, czyli jeśli nie istnieje mnożnik rzutów
                if dice_array[-2] == "+":  # ale, jeśli występuje czynnik addytywny na końcu kodu kostki
                    result_number = randint(1, int(dice_array[2])) + int(dice_array[-1])
                    return result_number
                elif dice_array[-2] == "-":  # jeśli na końcu od wyniku trzeba odjąć odpowiednią liczbę wg kodu
                    result_number = randint(1, int(dice_array[2])) - int(dice_array[-1])
                    return result_number
                else:  # jeśli nie istnieje  modyfikator + - wynik ilości rzutów
                    result_number = randint(1, int(dice_array[2]))
                    return result_number
        else:
            return "Niewłaściwa kostka!"  # jeśli kostka nie jest zgodna z oczekiwaniami
    except ValueError as e:
        return "Zły format zapisu kostki: " + str(e)  #przechwycenie błędu niewłaściwego kodowania kostki (np. k zamiast d)

rolled_dice = dice_input()
dice_result = dice_operation(rolled_dice)
print(dice_result)
