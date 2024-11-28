def main():
    kombinacje=0
    print("Możliwe kombinacje złożenia 100 zł z nominałów 2 zł, 5 zł i 10 zł:\n")
    for dycha in range(0,101,10):
        for piatka in range(0,101,5):
            for dwojka in range(0,101,2):
                if dycha+piatka+dwojka==100:
                    kombinacje+=1
                    print(f"10 zł: {dycha//10}, 5 zł: {piatka//5}, 2 zł: {dwojka//2}")
    print(f"\nŁączna liczba możliwych kombinacji: {kombinacje}")
main()