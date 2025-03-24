import random as rnd

nev = input("Kérem adja meg a karaktere nevét: ")

def olvas(eleresi):
    with open(eleresi, 'r', encoding="utf8") as f:
        return f.read()
val_cast = int(input("Válaszon egy karakter fajtát és írja be a számáz \n  1.Fekete macska : életerője 100, sebzése 15 \n 2.Narancs macska : életerője 120, sebzése 10 \n 3.Szürke macska : életerője 80, sebzése 20 \n"))




def karakter_general(stat, number):
    karakter = list()
    for i in range(number):
        dd = {
            "id" : i,
            "nev": nev,
        }
        if val_cast == 1:
            dd["elet"] = 100
            dd["sebzes"] = 15
        elif val_cast == 2:
            dd["elet"] = 120
            dd["sebzes"] = 10
        elif val_cast == 3:
            dd["elet"] = 80
            dd["sebzes"] = 20


def enemy_general(nevek, szam):
    enemy = list()
    for i in range(szam):
        d = {
            "id" : i,
            "nev": nevek[rnd.randint(0, len(nevek)-1)],
            "elet" : 100,
            "sebzes": rnd.randint(10,20)
      
        }
        enemy.append(d)
    return enemy


def harc(jatekos1, jatekos2):
    # HArc
    while jatekos1['elet'] > 0 and jatekos2['elet'] > 0:
        jatekos2['elet'] =- jatekos1['sebzes']
        # Ellenörizük hogy él a jatekos2
        if jatekos2['elet'] <= 0:
            break
        jatekos1['elet'] =- jatekos2['sebzes']
        
    if jatekos1['elet'] > 0:
        return jatekos1["id"]
    else:
        return jatekos2["id"]
        

        
# Ez csak akkor fut le ez a blcok amikor filet futtatjuk nem importáljuk

if __name__ == '__main__':
    szam = int(input("Adja meg hogy mennyi játékos szerepel: "))
    # nevek beolvasása
    nevek = olvas("names.txt")
    nevek_tomb = nevek.split("\n")
    print(nevek_tomb)
    # Játékosok generálása
    jatekosok = jatekosok_general(nevek_tomb)
    print(jatekosok[0])
    # HArc
    gyozelmek = []
    
    while szam !=0:
        gyozelmek.append(0)
        szam -= 1
    
    for i in range(len(jatekosok)):
        for j in range(i, len(jatekosok)):
            if i != j:
                harc(jatekosok[i], jatekosok[j])
                gyoztes  = harc(jatekosok[i], jatekosok[j])
                gyozelmek[gyoztes] += 1
    max = gyozelmek[0]
    gyoztes_index = 0
    for x in range(len(gyozelmek)):
        if gyozelmek[i] > max:
            max = gyozelmek[i]
            gyoztes_index = i
        
print(f"A játékosok győzteste: {jatekosok[gyoztes_index]["nev"]}")


#  Írják át  aprogrramot és kérdeze meg aze lején hogy hány játkossal futassav
