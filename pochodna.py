import math
def derivative(f,x,h=0.001):
    return (f(x+h)-f(x))/h

def kwadrat(x):
    return x**2

def main():
    print(derivative(math.sin,0))
    print(derivative(math.sin,1))
    print(derivative(kwadrat,1,0.000001))
    print(derivative(lambda x:x**2,1,0.000001))
main()