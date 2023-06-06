print("Dzień dobry")
elementy = int(input("Ile elementów chcesz wysłać?: "))
if elementy<=0:
    while elementy:
        break
waga = int(input("Podaj kolejno wagę elementów: "))
if waga in range(1, 11):
    while waga >= 1:
        kolejne_elementy = int(input("Podaj wagę kolejnych elementów: "))
        waga += kolejne_elementy
        print("Waga twoich elementów to :", waga)
        if kolejne_elementy in range(1, 11):
            continue
        else:
            print("Nie możemy wysłać takiej paczki")
            break
else:
    print("Nie możemy wysłać takiej paczki")