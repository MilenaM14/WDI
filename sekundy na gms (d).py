x=int(input("Podaj liczbe sekund "))
g=x//3600
m=(x%3600)//60
s=((x%3600)%60)

print(f"{g}:{m}:{s}")