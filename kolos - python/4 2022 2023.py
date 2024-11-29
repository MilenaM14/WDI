import math
def calka_przyblizona(f, x0, x1, dx=0.00001):
    suma=0
    x=x0
    while x<x1:
        suma+=f(x)*dx
        x+=dx
    return suma

def liniowa(x):
    return x

def main():
    calka=calka_przyblizona(liniowa,0,1)
    print(f"Całka dla funkcji y = x w przedziale [0, 1]: {calka}")
    calka_sin = calka_przyblizona(math.sin, 0, math.pi, dx=0.001)
    print(f"Całka dla funkcji sin(x) w przedziale [0, π]: {calka_sin}")
main()