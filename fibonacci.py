def fibo(n):
    if n<=0:
        return None
    if n==2 or n==1:
        return 1
    elif n>2:
        return fibo(n-1)+fibo(n-2)

def main():
    print(fibo(0))
    print(fibo(3))
    print(fibo(1))
main()