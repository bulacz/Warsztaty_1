print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w najwyżej 10 próbach")
'''
Dzielenie binarne. Komputer gra z użytkownikiem w grę zgadywania wymyślonej przez użytkownika liczby w zakresie 1-1000 
'''

min = 0  # deklaracja dolnej granicy przedziału poszukiwań
max = 1000  # deklaracja górwnej wartości przedziału poszukiwań
fun = True
fun_index = 10  # licnzik pętli - zabezpiecznie przed oszukiwaniem
while fun:
    if fun_index > 0:  # warunek uczciwej gry. Umowa na 10 prób.
        guess = int((int(max - min) / 2) + min) # ustawienie zmiennej "guess", którą komputer próbuje znaleźć
        print("Zgaduję: ", guess)
        answer = input("Za dużo (1) / Za mało (2) / OK: ")  # pobranie od użykownika odpowiedzi
        if answer == "1":  # jeśli liczba znaleziona przez komputer jest za duża...
            max = guess  # to w nowym wyszukiwaniu jest to górna granica przedziału
            fun_index -= 1  # dekrementacja licznika pętli zabawy
        elif answer == "2":  # jeśli liczba znaleziona przez komputer jest za mała...
            min = guess  # ... to staje się ona dolną granicą przedziału poszukiwań
            fun_index -= 1
        elif answer == "OK":  # jeśli komputer zgadł liczbę
            print ("Zgadłem!")
            fun = False
        else:  # wyłapanie błędu niewłaściwego klawisza odpowiedzi.
            print("Nie rozumiem... Mowiłem: ", guess)
    else:
        print("Nie oszukuj!")  # jeśli użytkownik oszukuje, tzn. komputer znalazł właściwą liczbę, ale user tego nie powie.
        fun = False  # przerwanie zabawy.


