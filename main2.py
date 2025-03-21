import random as rnd



def olvas(eleresi):
    with open(eleresi, 'r', encoding="utf8") as f:
        return f.read()

def jatekosok_general(nevek, szam):
    jatekosok = list()
    for i in range(szam):
        d = {
            "id" : i,
            "nev": nevek[rnd.randint(0, len(nevek)-1)],
            "elet" : 100,
            "sebzes": rnd.randint(10,20)
        }
        jatekosok.append(d)
    return jatekosok


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


#  Írják át  aprogrramot és kérdeze meg aze lején hogy hány játkossal futassa
