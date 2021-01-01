#pembelian buah dengan pimilahn
print("----PEMBELIAN BUAH DENGAN PEMILIHAN----")

#!!!GUNAKAN HURUF KECIL SAAT INPUT BUAH!!!

buah = {
    'apel' : 5000,
    'jeruk' : 8500,
    'mangga' : 7000,
    'duku' : 6500,
}
print("Daftar buah dan harga buah")
for key in buah:
    print (key, ":", buah[key])
print("Menu")
print("A. Tambah data buah")
print("B. Beli")
print("C. Hapus data buah")

pilihanMenu = input("Pilihan menu : ")
keys = list(buah.keys())

#jika pilihan tambah data buah
if pilihanMenu == "a" or pilihanMenu == "A":
    inputNamaBuah = input("Masukkan nama buah :")
    if inputNamaBuah == keys[0] or inputNamaBuah == keys[1] or inputNamaBuah == keys[2] or inputNamaBuah == keys[3]:
        print("Nama buah sudah ada")
    else:
        inputHargaBuah = int(input("Masukkan harga satuan :"))
        buah[inputNamaBuah] = inputHargaBuah
        print(buah)

#jika pilihan beli
elif pilihanMenu == "b" or pilihanMenu == "B":
    buah1 = 'apel'
    buah2 = 'jeruk'
    buah3 = 'mangga'
    buah4 = 'duku'
    sum = 0

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
        if tanya == "y" or tanya == "Y":
            dataBuah(sum)
        elif tanya == "n" or tanya == "N":
            print("-------------------------")
            print("Total harga: ", sum)

    dataBuah(sum)

#jika pemiliha hapus data
elif pilihanMenu == "c" or pilihanMenu == "C":
    inputNamaBuah = input("Masukkan nama buah :")
    if inputNamaBuah == keys[0] or inputNamaBuah == keys[1] or inputNamaBuah == keys[2] or inputNamaBuah == keys[3]:
        del buah[inputNamaBuah]
        print(buah)
    else:
        print("Nama buah tidak ditemukan")