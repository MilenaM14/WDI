def newton(n, k):
    if k < 0 or n < 0 or n < k:
        return None
    elif k == 0 or k == n:
        return 1
    else:
        return newton(n - 1, k - 1) + newton(n - 1, k)
def main():
    print(newton(-1, -1))
    print(newton(5, 0))
    print(newton(3, 2))
main()