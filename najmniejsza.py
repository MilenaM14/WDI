n=int(input("Podaj liczbe "))
for i in range(0,10):
    x=int(input("Podaj liczbe "))
    if n>x:
        n=x
print(f"Najmniejsza liczba to {n}")