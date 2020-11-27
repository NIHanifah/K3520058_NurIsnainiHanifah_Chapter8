#pembelian buah dengan pimilahn
print("----PEMBELIAN BUAH DENGAN PEMILIHAN----")

buah = {
    'apel' : 5000,
    'jeruk' : 8500,
    'mangga' : 7000,
    'duku' : 6500,
}

print("Daftar buah")
for x in buah:
    print(x, ":", buah[x])
print("Menu")
print("A. Tambah data buah")
print("B. Beli")

pilihanMenu = input("Pilihan menu : ")
a = "A"
b = "B"
#jika pilihan tambah data buah
keys = list(buah.keys())

#jika pilihan tambah data buah
if pilihanMenu == a:
    inputNamaBuah = input("Masukkan nama buah :")
    if inputNamaBuah == keys[0] or inputNamaBuah == keys[1] or inputNamaBuah == keys[2] or inputNamaBuah == keys[3]:
        print("Nama buah sudah ada")
    else:
        inputHargaBuah = int(input("Masukkan harga satuan :"))
        buah[inputNamaBuah] = inputHargaBuah
        print(buah)

#jika pilihan beli buah
elif pilihanMenu == b:
    buah1 = 'apel'
    buah2 = 'jeruk'
    buah3 = 'mangga'
    buah4 = 'duku'
    a = 'y'
    b = 'n'

#function penjumlahan buah
    def dataBuah(sum):
        namaBuah = input("Nama Buah :")
        kilo = int(input("Berapa Kg :"))
        tanya = input("Beli buah yang lain (y/n): ")
        if namaBuah == buah1:
            harga = buah['apel'] * kilo
        elif namaBuah == buah2:
            harga = buah['jeruk'] * kilo
        elif namaBuah == buah3:
            harga = buah['mangga'] * kilo
        elif namaBuah == buah4:
            harga = buah['duku'] * kilo
        sum += harga
        if tanya == a:
            dataBuah(sum)
        elif tanya == b:
            print("--------------------------")
            print("total harga: ", sum)

    sum = 0
    dataBuah(sum)
