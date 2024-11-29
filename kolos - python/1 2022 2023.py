def czy_pierwsza(x):
    dzielnik = [liczba for liczba in range(2,x) if x%liczba==0]
    return len(dzielnik) == 0
def main():
    liczby_pierwsze=[x for x in range(2,100) if czy_pierwsza(x)]
    print(f"Liczby pierwsze z zakresu 2-99: {liczby_pierwsze}")
main()
