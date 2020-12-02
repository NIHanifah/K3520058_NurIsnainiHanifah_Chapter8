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
