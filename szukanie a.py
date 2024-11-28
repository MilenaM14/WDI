def main():
    napis=input("Napisz słowo ")
    liczba=0
    for znak in napis:
        if znak=="a" or znak=="A":
            liczba+=1
    print(f"W napisie a lub A występuje {liczba} razy.")
main()
