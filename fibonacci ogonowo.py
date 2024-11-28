def fibo(n, a=1, b=1):
    if n<=0:
        return None
    if n==2 or n==1:
        return b
    return fibo(n-1,b,a+b)
def main():
    print(fibo(40))
    print(fibo(0))
    print(fibo(1))
    print(fibo(2))
main()