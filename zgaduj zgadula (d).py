import random
wylosowana=random.randint(1,10)

for proba in range(1,4):
    zgadywana=int(input(f"Próba {proba}: Podaj swoją liczbę: "))
    if zgadywana==wylosowana:
        print(f"Zgadłeś liczbę {wylosowana} w {proba} próbie.")
        break
    elif zgadywana<wylosowana:
        print("Podana liczba jest za mała.")
    else:
        print("Podana liczba jest za duża.")
else:
    print(f"Niestety nie zgadłes. Wylosowana liczba to: {wylosowana}")