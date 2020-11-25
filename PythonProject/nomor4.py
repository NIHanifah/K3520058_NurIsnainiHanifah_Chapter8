#program mengolah data sayur
print("----SAYUR----")
print('Menu')
print("A. Tambahkan data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan data sayur")

pilihan = input("Pilihan Anda :")
a = "A"
b = 'B'
c = 'C' 

sayur = ['bayam', 'wortel', 'kangkung', 'selada']

#jika pilihan menambah data sayur
if pilihan == a:
    inputSayur = input("Nama sayur :")
    sayur.append(inputSayur)
    print(sayur)
#jika pilihan menghapus sayur
elif pilihan == b:
    hapusSayur = input("Nama sayur :")
    i = 0
    while i < len(sayur):
        if hapusSayur == sayur[i]:
            del sayur[i]
            print(sayur)
            break
        elif hapusSayur != sayur[i]:
            print("Data tidak ditemukan")
            break
#jika pilihan menampilkan data sayur
elif pilihan == c:
    print(sayur)