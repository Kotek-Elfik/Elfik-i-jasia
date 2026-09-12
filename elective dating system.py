print("Czy nadajesz sie na randke?")
punkty = 0

wzrost = int(input("Podaj wzrost w cm"))
if wzrost >= 185:   
    punkty += 5
elif wzrost >= 175:
    punkty += 3
elif wzrost >= 170:
    punkty += 1

pieniadze = int(input("Ile zarabiasz miesiecznie w zl"))
if pieniadze >= 20000:
    punkty += 5
elif pieniadze >= 10000:
    punkty += 3
elif pieniadze >= 6000:
    punkty += 1

wspltmt = int(input("Czy macie wspolne tematy 1=tak, 0=nie"))
if wspltmt >= 1:
    punkty += 5

odleglosc = int(input("Jak daleko mieszkasz w km"))
if odleglosc <= 10:
    punkty += 5
elif odleglosc <= 20:
    punkty += 2
elif odleglosc <= 50:
    punkty += 1


if punkty >=15: print("Idziemy na randke!")
elif punkty >=10: print("Zobaczymy")    
elif punkty <=5: print("Wogole wiesz do kogo startujesz?")