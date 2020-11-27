#pembelian buah dengan pimilahn
print("----PEMBELIAN BUAH DENGAN PEMILIHAN----")

buah = {
    'apel' : 5000,
    'jeruk' : 8500,
    'mangga' : 7000,
    'duku' : 6500,
}

for key in buah:
    print (key, ":", buah[key])
print("Menu")
print("A. Tambah data buah")
print("B. Beli")
print("C. Hapus data buah")

pilihanMenu = input("Pilihan menu : ")
c = "A"
d = "B"
e = "C"

keys = list(buah.keys())
print(keys[0])

#jika pilihan tambah data buah
if pilihanMenu == c:
    inputNamaBuah = input("Masukkan nama buah :")
    inputHargaBuah = int(input("Masukkan harga satuan :"))
    if inputNamaBuah == keys[0] or inputNamaBuah == keys[1] or inputNamaBuah == keys[2] or inputNamaBuah == keys[3]:
        print("Nama buah sudah ada")
    else:
        buah[inputNamaBuah] = inputHargaBuah
        print(buah)