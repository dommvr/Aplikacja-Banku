import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

class klient:
    def __init__(self, id, imie, nr, saldo,):
        self.id = id
        self.imie = imie
        self.nr = nr
        self.saldo = saldo

klienci_banku = [klient(1, 'Jan Nowak', '001', 1457.23), 
            klient(2, 'Agnieszka Kowalska', '002', 3600.18), 
            klient(3, 'Robert Lewandowski', '003', 2745.03), 
            klient(4, 'Zofia Plucińska', '004', 7344.00), 
            klient(5, 'Grzegorx Braun', '005', 455.38 )]

def szukaj_po_nr(nr):
    for i in range(len(klienci_banku)):
        if nr == klienci_banku[i].nr:
            return i
    return False

def przelew(klient, nr, kwota):
    klient.saldo -= kwota
    klient_2 = klienci_banku[nr]
    klient_2.saldo += kwota

def lista_klientow():
    print('ID | IMIĘ I NAZWISKO | NR KONTA | SALDO')
    for klient_banku in klienci_banku:
        print(f'{klient_banku.id} | {klient_banku.imie} | {klient_banku.nr} | {klient_banku.saldo}')

def logowanie():
    user_input = int(input('ZALOGUJ SIĘ WYBIERAJĄC ID KLIENTA: '))
    login_id = user_input - 1
    if login_id < len(klienci_banku):
        klient_banku = klienci_banku[login_id]
        print(f'ZALOGOWANY KLIENT\nID: {klient_banku.id}\nMIĘ I NAZWISKO: {klient_banku.imie}\nNR KONTA: {klient_banku.nr}\nSALDO: {klient_banku.saldo} zł')
        user_input = input('WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAĆ PRZELEW: ')
        clear()
        if user_input != klient_banku.nr:
            klient_nr = szukaj_po_nr(user_input)
            if klient_nr != False:
                kwota = int(input('PODAJ KWOTĘ PRZELEWU: '))
                clear()
                if kwota <= klient_banku.saldo:
                    przelew(klient_banku, klient_nr, kwota)
                    print('PRZELEW ZOSTAŁ WYKONANY')
                    lista_klientow()
                else:
                    print('NIEWYSTARCZAJĄCE ŚRODKI NA RACHUNKU')
            else:
                print('NIEPRAWIDŁOWY NUMER KONTA')
        else:
            print('NIE MOŻESZ ZROBIĆ PRZELEWU NA WŁASNE KONTO.')
    else:
        print('LOGOWANIE NIEUDANE')

def menu():
    while True:
        print(f'WYBIERZ OPCJĘ:\n1 => LISTA WSZYSTKICH KLIENTÓW BANKU\n2 => LOGOWANIE\n3 => ZAKOŃCZ PROGRAM')
        user_input = int(input('WYBIERZ 1, 2 LUB 3: '))
        clear()
        if user_input == 1:
            lista_klientow()
            menu()
        elif user_input == 2:
            logowanie()
            exit()
        elif user_input == 3:
            exit()

if __name__ == '__main__':
    menu()