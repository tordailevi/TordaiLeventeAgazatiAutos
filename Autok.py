class Auto:
    def __init__(self, nev:str, gyartasi_datum:int):
        self.nev = str(nev)
        self.gyartasi_datum = int(gyartasi_datum)

    def __str__(self):
        return f"Autó: {self.nev}, Gyártási dátum: {self.gyartasi_datum}"