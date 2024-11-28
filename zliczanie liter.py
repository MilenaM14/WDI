def policz_litery(napis):
    sprawdzone_litery = ""

    for i, litera in enumerate(napis):
        if litera not in sprawdzone_litery:
            indeksy = [index for index, znak in enumerate(napis) if znak == litera]
            ilosc_wystapien = len(indeksy)
            print(f"{litera}: {' '.join(map(str, indeksy))} ({ilosc_wystapien})")
            sprawdzone_litery += litera
def main():
    napis = "Ala ma kota"
    policz_litery(napis)
main()
