x=int(input("Podaj liczbę a ja napiszę jaki to dzień tygodnia "))
def tydzien(x):
    match x:
        case 1:
            return "poniedziałek"
        case 2:
            return "wtorek"
        case 3:
            return "środa"
        case 4:
            return "czwartek"
        case 5:
            return "piątek"
        case 6|7:
            return "WEEKEND!"
        case _:
            return "Niepoprawna wartość"
def main():
    print(tydzien(x))
main()