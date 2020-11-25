#menampilkan buah paling mahal
print("----BUAH TERMAHAL----")
buah = {
    'apel' : 5000,
    'jeruk' : 8500,
    'mangga' : 7000,
    'duku' : 6500,
}

print("Buah termahal =", max(buah, key=buah.get))