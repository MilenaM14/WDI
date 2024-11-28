def main():
    poziom=int(input("Podaj liczbe poziomów "))
    for i in range(poziom):
        for j in range(poziom-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        print()
main()