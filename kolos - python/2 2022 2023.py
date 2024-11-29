cyfry_rzymskie={
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,}
def rzymska_na_arabska(liczba_rzymska):
    if not all(znak in cyfry_rzymskie for znak in liczba_rzymska):
        return None
    suma=0
    poprzednia_wartosc=0

    for znak in liczba_rzymska:
        obecna_wartosc=cyfry_rzymskie[znak]

        if obecna_wartosc>poprzednia_wartosc:
            suma+=obecna_wartosc-2*poprzednia_wartosc
        else:
            suma+=obecna_wartosc
        poprzednia_wartosc=obecna_wartosc
    return suma
def main():
    print(rzymska_na_arabska("VI"))
    print(rzymska_na_arabska("XIII"))
main()