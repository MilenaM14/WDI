slownik={
    '0':'zero',
    '1':'jeden',
    '2':'dwa',
    '3':'trzy',
    '4':'cztery',
    '5':'pięć',
    '6':'sześć',
    '7':'siedem',
    '8':'osiem',
    '9':'dziewięć',
}
def slownie(ciag_cyfr):
    litera=""
    for cyfra in ciag_cyfr:
        if cyfra in slownik:
            litera+=slownik[cyfra]+' '
    return litera
def main():
    print(slownie("1410"))
    print(slownie("14w10"))
main()