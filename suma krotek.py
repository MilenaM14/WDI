def suma_krotek(krotka):
    nowa_lista=[]
    for x,y in krotka:
        nowa_lista.append(x+y)
    return nowa_lista
def main():
    krotka1=[(1,2),(3,4),(5,6),(7,8)]
    krotka2=[('a','b'), ('a','c'), ('b','c')]
    print(suma_krotek(krotka1))
    print(suma_krotek(krotka2))
main()