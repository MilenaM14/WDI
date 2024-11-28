def suma1(lista):
    if len(lista) == 0:
        return None
    elif len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + suma1(lista[1:])
def suma2(lista, suma=0):
    match lista:
        case []:
            return None
        case [el]:
            return el + suma
        case glowa, *reszta:
            return suma2(reszta, glowa + suma)
def main():
    lista=[1,2,3,4,5]
    lista1=[]
    print(suma1(lista))
    print(suma2(lista))
    print(suma1(lista1))
    print(suma2(lista1))
main()