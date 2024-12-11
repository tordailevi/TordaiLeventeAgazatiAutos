def feladat1():
    print("I/A:")
    auto_neve:str=str(input("Autó neve: "))
    gyart_datum:int=int(input("Gyártási dátum:"))
    print("I/B:")
    if gyart_datum == 2024:
        print(f"Ez a(z) {auto_neve} friss gyártás.")
    elif gyart_datum < 2000:
        print(f"Ez a(z) {auto_neve} öreg autó.")
    else:
        print(f"Ez a(z) {auto_neve} átlagos korú.")
