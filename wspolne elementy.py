def wspolne_elementy(a, b):
    return list({wspolne for wspolne in a if wspolne in b})
def main():
    lista1 = [1, 2, 3, 4, 5, "Ala", "kot"]
    lista2 = [3, 4, 5, 4, "Ala"]
    print(wspolne_elementy(lista1, lista2))
main()