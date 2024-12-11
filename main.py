import bevezetes
import sorozat
import autom

bevezetes.feladat1()
randomszamok_lista = sorozat.feladat2()
e = sorozat.egyjegyuek_szama(randomszamok_lista)
sorozat.konzol_kiir(e)
sorozat.file_kiir(e)
autok_lista = autom.beolvasas()
autok_szama = autom.flotta(autok_lista)
legfiatalabb_auto = autom.legfiatalab(autok_lista)
atlagkor = autom.atlag_kor(autok_lista)
autom.kiiras(autok_lista, autok_szama, legfiatalabb_auto, atlagkor)