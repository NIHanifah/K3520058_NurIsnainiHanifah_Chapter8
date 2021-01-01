#membuat list
print("-----MEMBUAT LIST-----")
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print("a = ", a)
print("b = ", b)

#menyisipkan nilai di antara nilai
print("-----MENYISIPKAN NILAI-----")
a.insert(3, 10)
print("a(dengan sisipan) = ",a)
b.insert(2, 15)
print("b(dengan sisipan) = ", b)

#menyisipkan nilai di akhri
print("-----MENYISIPKAN NILAI DI TENGAH-----")
a.append(4)
print("a (sisipan akhir) = ", a)
b.append(8)
print("b (sisipan akhir) = ", b)

#sorting
print("-----SORTING ASCANDING-----")
a.sort()
print("Urutan a = ", a)
b.sort()
print("Urutan b = ", b)

#penggabungan list
print("----Pengambilan Sub a dan Sub b----")
c = a[0:8]
d = b[2:10]
print("c = ", c)
print("d = ", d)

#membuat list e yang hasil dari penjumlahan dua list
print("----LIST E(PENJUMLAHAN C DAN D)----")
e = []

i = 0
for i in range(len(c)):
    jumlahcd = c[i] + d[i]
    e.insert(i, jumlahcd)
    i += 1

print("c = ", c)
print("d = ", d)
print("e =", e)

#mengubah list e ke dalam tuple
print("----MENGUBAH LIST K TUPLE----")
eTuple = tuple(e)
print("eTuple =", eTuple)

#mencari nilai min, maks, dan jumlah dalam elem 5
print("----MENCARI NILAI MIN, MAKS, DAN JUMLAH----")
#min
print("Nilai minimal = ", min(eTuple))
#maks
print("Nilai maksimal = ", max(eTuple))
#jumlah
print("Jumlah nilai = ", sum(eTuple))

#membuat string
print("----PPENYUSUN HURUF----")
myString = "python adalah bahasa pemrogaman yang menyenangkan"
penyusunMyString = set(myString)
print(penyusunMyString)

#mengubah string ke list
listString = list(penyusunMyString)

#mengurutkan string
print("---------MENGURUTKAN HURUF--------")
listString.sort()
print(listString)

#program mengolah data sayur
print("----SAYUR----")
print('Menu')
print("A. Tambahkan data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan data sayur")

pilihan = input("Pilihan Anda :")

sayur = ['bayam', 'wortel', 'kangkung', 'selada']

#jika pilihan menambah data sayur
if pilihan == "a" or pilihan == "A":
    inputSayur = input("Nama sayur :")
    if inputSayur == sayur[0] or inputSayur == sayur[1] or inputSayur == sayur[2] or inputSayur == sayur[3]:
        print("Data sudah ada")
    else:
        sayur.append(inputSayur)
        print(sayur)
#jika pilihan menghapus sayur
elif pilihan == "b" or pilihan == "B":
    inputSayur = input("Nama sayur :")
    if inputSayur == sayur[0] or inputSayur == sayur[1] or inputSayur == sayur[2] or inputSayur == sayur[3]:
        sayur.remove(inputSayur)
        print(sayur)
    else:
        print("Nama sayur tidak ditemukan")


#jika pilihan menampilkan data sayur
elif pilihan == "c" or pilihan == "C":
    print(sayur)
