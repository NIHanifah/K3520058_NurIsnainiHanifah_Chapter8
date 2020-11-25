#program pembelian buah
print("----PEMBELIAN BUAH----")
buah = {
    'apel' : 5000,
    'jeruk' : 8500,
    'mangga' : 7000,
    'duku' : 6500,
}

print("Daftar  buah = ")
for x in buah:
    print(x)
namaBuah = input("Nama Buah :")
kilo = int(input("Berapa Kg :"))

buah1 = 'apel'
buah2 = 'jeruk'
buah3 = 'mangga'
buah4 = 'duku'

if namaBuah == buah1:
    harga = buah['apel'] * kilo
elif namaBuah == buah2:
    harga = buah['jeruk'] * kilo
elif namaBuah == buah3:
    harga = buah['mangga'] * kilo
elif namaBuah == buah4:
    harga = buah['duku'] * kilo

print("Total harga buah = ", harga)