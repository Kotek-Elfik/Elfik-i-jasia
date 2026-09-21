def pole_lub_objentosc(a):
    if a == 'a':
        a = 'pole'
    elif a == 'b':
        a = 'objętość'
    b = input(f'Wybierz {a} czego chcesz obliczy: \n'
              'a = sześcianu\n'
              'b = prostopałościanu\n'
              'c = graniastosłupa\n'
              'd = walca\n'
              'e = kuli\n'
              'Twoj wybor: ')

    if a == 'pole':
        if a == 'a':
            pole_powierzchni_szescianu()
        elif a == 'b':
            pole_powierzchni_prostopaloscianu()
        elif a == 'c':
            pole_powierzchni_graniastoslupa()
        elif a == 'd':
            pole_powierzchni_walca()
        elif a == 'e':
            pole_powierzchni_kuli()
        else:
            print("NIE MA TAKIEJ OPCII")
    elif a == 'objętość':
        if b == 'a':
            objentosc_szescianu()
        elif b == 'b':
            objentosc_prostopaloscianu()
        elif b == 'c':
            obentosc_graniastoslupa()
        elif b == 'd':
            objentosc_walca()
        elif b == 'e':
            objentosc_kuli()
        else:
            print("NIE MA TAKIEJ OPCII")


def obwod():
    a = input('Wybierz obwód czego chcesz obliczy: \n'
              'a = kwadratu\n'
              'b = prostokątu\n'
              'c = równoległoboku\n'
              'd = trapezu\n'
              'e = trójkątu\n'
              'Twoj wybor: ')

    if a == 'a':
        obwod_kwadratu()
    elif a == 'b':
        obwod_rostokatu()
    elif a == 'b':
        obwod_rownolegloboku()
    elif a == 'b':
        obwod_trapezu()
    elif a == 'b':
        print()
    else:
        print("NIE MA TAKIEJ OPCII")


# ---------------------------------
def pole_powierzchni_szescianu():
    a = float(input('Strona szescianu: '))
    result = a ** 2 * 6
    print(f'Pole szescianu = {result}')


def pole_powierzchni_prostopaloscianu():
    a = float(input('1 strona prostopaloscianu: '))
    b = float(input('2 strona prostopaloscianu: '))
    c = float(input('3 strona prostopaloscianu: '))
    result = 2 * a * b + 2 * a * c + 2 * b * c
    print(f'Pole prostopaloscianu = {result}')


def pole_powierzchni_graniastoslupa():
    a = float(input('Krawedz podstawy prostopaloscianu: '))
    b = float(input('Krawedz boku prostopaloscianu: '))
    result = a ** 2 * 2 + a * b
    print(f'Pole graniastoslupa = {result}')


def pole_powierzchni_walca():
    a = float(input('Wprowadz: r = '))
    b = float(input("Wprowadz wysokosc: h = "))
    result = a ** 2 * 3.14 * 2 + 2 * 3.14 * a * b
    print(f'Pole walca = {result}')


def pole_powierzchni_kuli():
    a = float(input('Wprowadz: r = '))
    result = a ** 2 * 4 * 3.14
    print(f'Pole kuli = {result}')


# ---------------------------------
def objentosc_szescianu():
    a = float(input('Strona szescianu: '))
    result = a ** 3
    print(f'Obentosc szescianu = {result}')


def objentosc_prostopaloscianu():
    a = float(input('1 strona prostopaloscianu: '))
    b = float(input('2 strona prostopaloscianu: '))
    c = float(input('3 strona prostopaloscianu: '))
    result = a * b * c
    print(f'Obentosc prostopaloscianu = {result}')


def obentosc_graniastoslupa():
    a = float(input('Krawedz podstawy prostopaloscianu: '))
    b = float(input('Wysokosc prostopaloscianu: '))
    result = a ** 2 + b
    print(f'Pole graniastoslupa = {result}')


def objentosc_walca():
    a = float(input('Wprowadz: r = '))
    b = float(input("Wprowadz wysokosc: h = "))
    result = a ** 2 * 3.14 + b
    print(f'Obentosc walca = {result}')


def objentosc_kuli():
    a = float(input('Wprowadz: r = '))
    result = a ** 3 * 4 / 3 * 3.14
    print(f'Obentosc kuli = {result}')


# ----------------------------------
def obwod_kwadratu():
    a = float(input('Strona kwadratu: '))
    result = a * 4
    print(f'Obwod kwadrtu = {result}')


def obwod_rostokatu():
    a = float(input('Wprowadz dlugosc: '))
    b = float(input('Wprowadz szerokosc: '))
    result = a * 2 + b * 2
    print(f'Obwod prostokątu = {result}')


def obwod_rownolegloboku():
    a = float(input('Wprowadz dlugosc: '))
    b = float(input('Wprowadz szerokosc: '))
    result = a * 2 + b * 2
    print(f'Obwod rownolegloboku = {result}')


def obwod_trapezu():
    a = float(input('1 krawendz trapezu: '))
    b = float(input('2 krawendz trapezu: '))
    c = float(input('3 krawendz trapezu: '))
    d = float(input('4 krawendz trapezu: '))
    result = a + b + c + d
    print(f'Obwod trapezu = {result}')


def obwod_trojkanta():
    a = float(input('1 krawendz trojkanta: '))
    b = float(input('2 krawendz trojkanta: '))
    c = float(input('3 krawendz trojkanta: '))
    result = a + b + c
    print(f'Obwod trojkanta = {result}')


wybor = input('Wybierz dostępną opcję: \n'
              'a = pole\n'
              'b = objętość\n'
              'c = obwód\n'
              'Twój wybór: ')

if wybor == 'a' or wybor == 'b':
    pole_lub_objentosc(wybor)
elif wybor == 'c':
    obwod()
else:
    print('Nie ma takiej opcii')
