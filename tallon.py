## 1-2.feladat Írj programot, beolvassa a felhasználó nevét, majd köszön neki!

#Változók

nev, szovegkiir = "", ""

nev = input("Hogy hívnak?")

szovegkiir = f"Hello {nev}!"
print(szovegkiir)

## 3.Írj programot, ami beolvas egy számot, majd kiírja a kétszeresét!

#Változók

szam = input("Mondj egy számot: ")
szam = int(szam)
print("A szám kétszerese:", szam * 2)

## 4.feladatÍrj programot, ami beolvas két számot, majd kiírja:
## a. az összegüket;
## b. különbségüket;
## c. szorzatukat;
## d. hányadosukat, ha lehet! 

## Változók

szam1 = input("Adj meg egy számot: ")
szam1 = int(szam1)
szam2 = input("Adj meg egy másik számot: ")
szam2 = int(szam2)

print("Az összegük:", szam1 + szam2)
print("A különbségük:", szam1 - szam2)
print("A szorzatuk:", szam1 * szam2)

if szam2 != 0:
    print("A hányadosuk:", szam1 / szam2)
else:
    print("A hányadosukat nem értelmezzük, mert a második szám nulla.")


## 5.Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!

## Változók

a = int(input("Kérlek adj  meg egy számot:"))
b = int(input("Kérlek adj meg egy másik számot:"))

if a > b:

    print("Az első szám nagyobb", a)

else: 

    print("A második szám nagyobb",b)


## 6. Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!

# Változók

a = int(input("Első szám: "))
b = int(input("Második szám: "))
c = int(input("Harmadik szám: "))

minimum = a
if b < minimum:
    minimum = b
if c < minimum:
    minimum = c

print("A három szám közül a legkisebb:", minimum)

## 7. Írj programot, ami beolvassa a háromszög oldalainak hosszát, és megmondja, hogy ilyen oldalakkal szerkeszthető-e háromszög!

## Változók

a = float(input("Add meg az első oldal hosszát: "))
b = float(input("Add meg a második oldal hosszát: "))
c = float(input("Add meg a harmadik oldal hosszát: "))

if a + b > c and a + c > b and b + c > a:

    print("Ilyen oldalakkal szerkeszthető háromszög.")
else:
    print("Ilyen oldalakkal nem lehet háromszöget szerkeszteni.")

## 8.Írj programot, mely beolvas két pozitív egész számot, és kiírja a számtani és mértani közepüket! A gyökvonáshoz használd a Math.Sqrt() függvényt! (Itt kellet az AI segítsége.)

import math

a = int(input("Első szám"))
b = int(input("Második szám"))

szamtani_kozep = (a + b) /2
geometriai_kozep = math.sqrt (a * b)

print("A számok számatni  közepe", szamtani_kozep)
print("A számok geometriai közepe", geometriai_kozep)

## END 