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

#jika pilihan tambah data buah
if pilihanMenu == c:
    inputNamaBuah = input("Masukkan nama buah :")
    inputHargaBuah = int(input("Masukkan harga satuan :"))
    for x in buah.keys():
        if inputNamaBuah == x:
            print("Nama buah sudah ada")
            break
        else:
            buah[inputNamaBuah] = inputHargaBuah
            print(buah)
            break

#jika pilihan beli
elif pilihanMenu == d:
    buah1 = 'apel'
    buah2 = 'jeruk'
    buah3 = 'mangga'
    buah4 = 'duku'
    a = 'y'
    b = 'n'
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
        if tanya == a:
            dataBuah(sum)
        elif tanya == b:
            print("-------------------------")
            print("Total harga: ", sum)

    dataBuah(sum)

#jika pemiliha hapus data
elif pilihanMenu == e:
    print(buah)
    inputNamaBuah = input("Masukkan nama buah :")
    i = 0
    while i < len(buah):
        for xx in buah:
            if inputNamaBuah == xx:
                del buah[inputNamaBuah]
                print(buah)
            elif inputNamaBuah != xx:
                print("Nama buah tidak ditemukan")
        i += 1
            
