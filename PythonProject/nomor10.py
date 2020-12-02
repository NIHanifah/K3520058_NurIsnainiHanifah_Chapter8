#pembelian buah dengan perulangan
print("----PEMBELIAN BUAH DENGAN PERULANGAN----")

#!!!GUNAKAN HURUF KECIL SAAT INPUT BUAH!!!

buah = {
    'apel' : 5000,
    'jeruk' : 8500,
    'mangga' : 7000,
    'duku' : 6500,
}

buah1 = 'apel'
buah2 = 'jeruk'
buah3 = 'mangga'
buah4 = 'duku'

sum = 0

#function eenghitungan buah
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