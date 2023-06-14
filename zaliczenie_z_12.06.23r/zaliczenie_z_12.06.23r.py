opcje = "Wybierz jedną z opcji: " \
        "sprzedaz, zakup, konto, magazyn, koniec: "
#firma
rower_cena = 500
rower_ilosc_firma = 10
koło_cena = 100
koło_ilosc_firma = 30
opona_cena = 50
opona_ilosc_firma = 50
konto = int(input("Podaj swoje konto: "))
#                 1 cena 2 ilosc
'''
wartość_początkowa_towaru = rower_cena*rower_ilosc_firma+koło_ilosc_firma*koło_cena+opona_ilosc_firma*opona_cena
'''
magazyn_firma = ["rower", "$", rower_cena, "szt: ", rower_ilosc_firma, "koło", "$", koło_cena, "szt: ", koło_ilosc_firma, "opona", "$", koło_cena, "szt: ", koło_ilosc_firma]
kupione_rowery = 0
kupione_koła = 0
kupione_opony = 0
'''wartość_towaru_do_rozliczenia = kupione_rowery*rower_cena+kupione_koła*koło_cena+kupione_opony*opona_cena
saldo = konto - wartość_towaru_do_rozliczenia'''
#Magazyn
rower_cena = 500
rower_ilosc_magazyn = 50
koło_cena = 100
koło_ilosc_magazyn = 200
opona_cena = 50
opona_ilosc_magazyn = 300
#                 1 cena 2 ilosc
magazyn = ["rower", "$", rower_cena, "szt: ", rower_ilosc_magazyn, "koło", "$", koło_cena, "szt: ", koło_ilosc_magazyn, "opona", "$", koło_cena, "szt: ", koło_ilosc_magazyn]
"""decyzja = input("Czy chcesz kontynuować?: tak/nie")
sprzedawanie = input("Co sprzedajesz? (rower, koło, opona): ")
kupowanie = input("Co kupujesz?" "(rower, koło, opona): ")"""
kontynuacja = True
while kontynuacja:
    komendy = input(opcje)
    if "koniec" in komendy:
        print(magazyn_firma)
        print(magazyn)
        print(konto)
        break
    if not konto > 0:
        print("Nie masz pieniędzy!")
        print(opcje)
        break
    if konto > 0:
        None
    if "zakup" in komendy:
        kupowanie = input("Co kupujesz?" "(rower, koło, opona): ")
        if "rower" in kupowanie:
            konto -= rower_cena
            rower_ilosc_firma += 1
            kupione_rowery += 1
            rower_ilosc_magazyn -= 1
            print("Stan konta: ", konto)
            print("Ilość rowerów na magazynie: ", rower_ilosc_magazyn)
            print("Ilość rowerów w firmie: ", rower_ilosc_firma)
            if rower_ilosc_magazyn == 0:
                print("Brak w magazynie!")
                break

        if "koło" in kupowanie:
            konto -= koło_cena
            kupione_koła += 1
            koło_ilosc_firma += 1
            koło_ilosc_magazyn -= 1
            print("Stan konta: ", konto)
            print("Ilość kół na magazynie: ", koło_ilosc_magazyn)
            print("Ilość kół w firmie: ", koło_ilosc_firma)
            if koło_ilosc_magazyn == 0:
                print("Brak w magazynie!")
                break

        if "opona" in kupowanie:
            konto -= opona_cena
            kupione_opony += 1
            opona_ilosc_magazyn -= 1
            opona_ilosc_firma += 1
            print("Stan konta: ", konto)
            print("Ilość opon na magazynie: ", opona_ilosc_magazyn)
            print("Ilość opon na firmie: ", opona_ilosc_firma)
            if opona_ilosc_magazyn == 0:
                print("Brak w magazynie!")
                break
        if "koniec" in kupowanie:
            None

    if "konto" in komendy:
        print(konto)
        None

    if "sprzedaz" in komendy:
        sprzedawanie = input("Co sprzedajesz? (rower, koło, opona): ")
        if "rower" in sprzedawanie:
            if rower_ilosc_firma == 0:
                break
            if rower_ilosc_firma> 0:
                    konto += rower_cena
                    rower_ilosc_firma -= 1
                    print("Stan konta: ", konto)
                    print("Ilość rowerów: ", rower_ilosc_firma)
        if "koło" in sprzedawanie:
            if koło_ilosc_firma == 0:
                break
            if koło_ilosc_firma> 0:
                konto += koło_cena
                koło_ilosc_firma -= 1
                print("Stan konta: ", konto)
                print("Ilość koło: ", koło_ilosc_firma)
        if "opona" in sprzedawanie:
            if opona_ilosc_firma == 0:
                break
            if opona_ilosc_firma > 0:
                konto += opona_cena
                opona_ilosc_firma -= 1
                print("Stan konta: ", konto)
                print("Ilość opona: ", opona_ilosc_firma)
        if "koniec" in sprzedawanie:
                        print(konto)
                        None

'''    
    if "lista" in komendy:
        print("MAGAZYN: ", magazyn)
        print("FIRMA: ", magazyn_firma)
        None
'''

'''
    if "saldo" in komendy:
        print(konto-wartość_towaru_do_rozliczenia)
        None
'''






#for [0] in produkty:
# print(produkty)
#sprzedaz = ["saldo", "sprzedaz", "zakup", "konto", "lista", "magazyn", "przeglad", "koniec"]
#komendy = produkty
#while komendy (input("Wybierz: (saldo, sprzedaz, zakup, konto, lista, magazyn, przeglad, koniec): ")):
