kontakty = {('Jan', 'Kowalski'):"123456789",
            ('Adam', 'Nowak'):"987654321",
            ('Adam', 'Kowalski'):"600300900"}
def numery(kontakt,nazwisko):
    return[num for (imie, nazw), num in kontakty.items() if nazw==nazwisko]
def main():
    print("Numer telefonu Adama Nowaka:", kontakty[("Adam", "Nowak")])
    numery_kowalskich = numery(kontakty, "Kowalski")
    print("Numery telefonów osób o nazwisku Kowalski:", numery_kowalskich)
main()