#wersja 1
#zadanie 1
from math import pi as PI
r = float(input())
print(PI * r ** 2)
#zadanie 2
n = int(input())
i = 0
while i < n:
    print("kocham programować")
    i = i + 1
#zadanie 3
suma = 0

while True:
    x = input("Podaj liczbę: ")

    if x == "stop":
        break

    suma += int(x)

print(suma)
#zadanie 4
suma = 0
ile = 0
while True:
    x = input("Podaj liczbę: ")
    if x == "stop":
        break
suma += int(x)
ile += 1
print("Średnia =", suma / ile)
#zadanie 5
from random import randint
punkty = 0
for i in range(6):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
odp = int(input(f"Ile wynosi {a} * {b}? "))
if odp == a * b:
    punkty += 1
else:
    if punkty == 6:
        ocena = 6
    elif punkty == 5:
        ocena = 5
    elif punkty == 4:
        ocena = 4
    elif punkty == 3:
        ocena = 3
    elif punkty == 2:
        ocena = 2
    else:
        ocena = 1
print("Liczba punktów:", punkty)
print("Ocena:", ocena)
#wersja 2 
    #zadanie 1
a = float(input("a: "))
b = float(input("b: "))
h = float(input("h: "))
print(f"ostroslup o podst {ab} i h = {h} ma V = {ab*h/3}")
    # #zadanie 2
from random import randint
x = randint(1, 100)
proba = 1
max_prob = 3
a = int(input(f"proba {proba} z {max_prob}. Podaj liczbe od 1 do 100: "))
while proba < max_prob:
    if a == x:
        print(f"zgadles za {proba} proba")
        break
    elif a > x:
        print("za wysoko")
    else:
        print("za nisko")
    proba += 1
    a = int(input(f"proba {proba} z {max_prob}. Podaj liczbe od 1 do 100: "))
else:
    print(f"nie zgadles liczba x to {x}")
    #zadanie 3
liczby = []
najwieksza_liczba = 0
l = input("podaj liczbe: ").strip()
while True:
    if l.lower() == "stop":
        print(f"najwieksa liczba to {najwieksza_liczba}")
        break
    else:
        liczba_float = float(l)
        liczby.append(liczba_float)
        l = input("podaj liczbe: ")
    if liczba_float > najwieksza_liczba or najwieksza_liczba == 0:
        najwieksza_liczba = liczba_float
    #zadanie 4
a = float(input("podaj a: "))
b = float(input("podaj b: "))
c = float(input("podaj c: "))
if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a**2:
    print("z tych odcinkow mozna zbudowac trojkat prostokatny")
else:
    print("z tych odcinkow nie mozna zbudowac trojkata prostokatnego")
    #zadanie 5
import random
n = int(input("podaj n: "))
if n < 3:
    print("n musi byc wieksze od 3")
else:
    cut1 = random.randint(0, n)
    cut2 = random.randint(0, n)
    p1 = min(cut1, cut2)
    p2 = max(cut1, cut2)
    odcinek1 = p1
    odcinek2 = p2 - p1
    odcinek3 = n - p2
    print(f"odcinek1: {odcinek1}, odcinek2: {odcinek2}, odcinek3: {odcinek3}")
#wersja 3
    #zadanie 1
    a = float(input("a: "))
    print(f"szescia o boku {a} ma v = {a3}")
    #zadanie 2
    from random import randint
    import random
    for i in range(10):
        liczba = random.randint(1, 100)
        print(liczba)
    #zadanie 3
    suma = 0
    ile = 0
while True:
    x = input("Podaj liczbę: ")
    if x == "stop":
        print(f"Suma = {suma} Średnia = {suma / ile}")
        break
    suma += int(x)
    ile += 1
    #zadanie 4
a = int(input())
b = int(input())
c = int(input())
if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
    print("to trojkat prostokatny")
    if a == b == c:
        print("to trojkat rownoboczny")
    else:
        print("to trojkat roznoboczny")
else:
    print("to nie jest trojkat prostokatny")
#zadanie 5
k = int(input())
m = int(input())
print("reszta z dzielenia =", k % m)
#zadanie 6
k = int(input())
m = int(input())
print("Liczba dzieli się", k // m, "razy")