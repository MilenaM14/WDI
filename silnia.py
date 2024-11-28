def main():
    while True:
        n=int(input("Podaj liczbę n (0 lub 10 kończy pętle) "))
        if n<0:
            print("Liczba nie może być ujemna.")
            continue
        if n==0 or n==10:
            print("Koniec programu.")
            break
        silnia=1
        for i in range(1,n+1):
            silnia*=i
        print(silnia)
main()
