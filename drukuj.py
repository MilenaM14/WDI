import sys

def drukuj(*args, sep=" ", end="\n"):
    wynik = sep.join(str(arg) for arg in args) + end
    sys.stdout.write(wynik)

def main():
    drukuj(192, 168, 0, 1, sep=":")
    temperatura = 36.6
    drukuj("Temperatura wynosi", temperatura, "stopni")
    for _ in range(10):
        drukuj("*", end="")
main()