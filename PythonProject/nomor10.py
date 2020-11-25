#pembelian buah dengan perulangan
print("----PEMBELIAN BUAH DENGAN PERULANGAN----")

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
a = 'y'
b = 'n'

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
    if tanya == a:
        dataBuah(sum)
    elif tanya == b:
        print("-------------------------")
        print("Total harga: ", sum)

dataBuah(sum)