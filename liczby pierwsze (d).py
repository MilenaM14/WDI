def main():
    print("Liczby pierwsze w zakresie od 2 do 99:")
    for liczba in range(2,100):
        for dzielnik in range(2,liczba):
            if liczba%dzielnik==0:
                break
        else:
            print(liczba,end=" ")
main()