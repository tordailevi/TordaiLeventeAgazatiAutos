from Autok import Auto

def beolvasas():
    autok_lista=[]
    fajlom = open("auto.txt", "r", encoding="UTF-8")
    elso_sor = fajlom.readline()
    sorok_lista = fajlom.readlines()

    for i in range(0, len(sorok_lista), 1):
        sor = sorok_lista[i].strip()
        sor_lista = sor.split("$")
        autok = Auto(sor_lista[0], sor_lista[1])
        autok_lista.append(autok)
    fajlom.close()
    return autok_lista

def flotta(autok_lista):
    autok_szama = len(autok_lista)
    return autok_szama

def legfiatalab(autok_lista):
    legfiatalabb_auto = autok_lista[0]
    for auto in autok_lista:
        if auto.gyartasi_datum < legfiatalabb_auto.gyartasi_datum:
            legfiatalabb_auto = auto 
    return legfiatalabb_auto

def atlag_kor(autok_lista):
    osszes=0
    for i in range(0, len(autok_lista)):
        auto = autok_lista[i]
        osszes += auto.gyartasi_datum
        atlagkor = osszes % len(autok_lista)
        return atlagkor

def kiiras(autok_lista, autok_szama, legfiatalabb_auto, atlagkor):
    print("III/Flotta:")
    print(f"Autók száma: {autok_szama}.\n")
    print("III/Legfiatalabb")
    print(f"A legfiatalabb autó: {legfiatalabb_auto.nev} ({legfiatalabb_auto.gyartasi_datum})\n")
    print("III/Átlag kor")
    print(f"Az autók átlagos kora: {atlagkor} év.\n")