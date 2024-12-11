import random
def feladat2():
    print("II/A, B, C:")
    randomszamok_lista=[]
    x:int=0
    for i in range(0, 5, 1):
        lottoszamok = random.randint(1,99)
        randomszamok_lista.append(lottoszamok)
        x += 1
        if x == 5:
            print(lottoszamok)
        else:
            print(lottoszamok, end=";")
    return randomszamok_lista


def egyjegyuek_szama(randomszamok_lista):
    e:int=0
    for i in range(0, len(randomszamok_lista), 1):
        if randomszamok_lista[i] < 10:
            e += 1
    return e