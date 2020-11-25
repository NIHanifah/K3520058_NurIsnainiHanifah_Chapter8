#menetukan rerata buah satuan
print("----RERATA BUAH SATUAN----")

buah = {
    'apel' : 5000,
    'jeruk' : 8500,
    'mangga' : 7000,
    'duku' : 6500,
}

#function menentukan rerata buah
def rerata(buah):
    print("Jumlah harga buah = ", sum(buah.values()))
    print("Jumlah banyak buah =", len(buah))
    rerata = sum(buah.values())/len(buah)
    print("Rerata harga buah = ", int(rerata))

rerata(buah)
