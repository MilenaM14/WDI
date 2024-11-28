def slowa_na_liczby(napis):
    dziesiatki = {
        "dwadzieścia": 20,
        "trzydzieści": 30,
        "czterdzieści": 40,
        "pięćdziesiąt": 50
    }

    jednostki = {
        "zero": 0,
        "jeden": 1,
        "dwa": 2,
        "trzy": 3,
        "cztery": 4,
        "pięć": 5,
        "sześć": 6,
        "siedem": 7,
        "osiem": 8,
        "dziewięć": 9
    }

    slowa = napis.split()
    wynik = 0
    if slowa[0] in dziesiatki:
        wynik += dziesiatki[slowa[0]]
    if len(slowa) > 1 and slowa[1] in jednostki:
        wynik += jednostki[slowa[1]]
    return wynik


def main():
    print(slowa_na_liczby("dwadzieścia jeden"))
    print(slowa_na_liczby("czterdzieści pięć"))
    print(slowa_na_liczby("pięćdziesiąt trzy"))
    print(slowa_na_liczby("trzydzieści"))
main()