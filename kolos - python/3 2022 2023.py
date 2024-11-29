def zwykla_rekurencja(n):
    if n==1:
        return 6
    elif n==2:
        return 16
    else:
        return 4*(zwykla_rekurencja(n-1)-zwykla_rekurencja(n-2))

def ogonowa_rekurencja(n, a1=6, a2=16):
    if n==1:
        return a1
    elif n==2:
        return a2
    else:
        return ogonowa_rekurencja(n-1, a2, 4*(a2-a1))
def main():
    print(zwykla_rekurencja(1))
    print(zwykla_rekurencja(2))
    print(zwykla_rekurencja(3))
    print(ogonowa_rekurencja(1))
    print(ogonowa_rekurencja(2))
    print(ogonowa_rekurencja(3))
main()