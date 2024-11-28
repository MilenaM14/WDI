def lata(od,do):
    return[rok for rok in range(od,do+1) if (rok%4==0 and rok%100!=0 or rok%400==0)]
def main():
    print(lata(1900,2000))
main()