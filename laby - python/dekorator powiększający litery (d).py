import sys

slownik = {
    '0': 'zero',
    '1': 'jeden',
    '2': 'dwa',
    '3': 'trzy',
    '4': 'cztery',
    '5': 'pięć',
    '6': 'sześć',
    '7': 'siedem',
    '8': 'osiem',
    '9': 'dziewięć',
}

def slownie(ciag_cyfr):
    litera = ""
    for cyfra in ciag_cyfr:
        if cyfra in slownik:
            litera += slownik[cyfra] + " "
    return litera.strip()

def stworz_napis(*args, sep=" ", end="\n"):
    return sep.join(str(arg) for arg in args) + end

def na_wielkie_litery(funkcja):
    def wrapper(*args, **kwargs):
        wynik = funkcja(*args, **kwargs)
        return wynik.upper()
    return wrapper

@na_wielkie_litery
def slownie_dekorowane(ciag_cyfr):
    return slownie(ciag_cyfr)

@na_wielkie_litery
def stworz_napis_dekorowane(*args, sep=" ", end="\n"):
    return stworz_napis(*args, sep=sep, end=end)

def main():
    print(slownie("1410"))
    print(slownie_dekorowane("1410"))
    print(stworz_napis("Ala", "ma", "kota", sep="-"))
    print(stworz_napis_dekorowane("Ala", "ma", "kota", sep="-"))
main()