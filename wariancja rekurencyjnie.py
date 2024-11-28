def main():
    lista1 = [3, 3, 3, 3]
    lista2 = [5, 6, 7, 8, 9]
    lista3= [1, 2, 3, 4]
    print(srednia(lista1, len(lista1)))
    print(srednia(lista2, len(lista2)))
    print(srednia(lista3, len(lista3)))
    
def srednia(lista, dlugosc, suma=0):
    match lista:
        case []:
            return suma / dlugosc, 0
        case glowa, *reszta:
            x, w = srednia(reszta, dlugosc, glowa + suma)
            w += (glowa - x) ** 2 / dlugosc
            return x, w
main()