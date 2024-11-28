def main():
    napis=input("Napisz słowo ")
    for indeks,znak in enumerate(napis,1):
        if znak=="a" or znak=="A":
            print(indeks)
main()