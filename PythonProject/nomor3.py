#penyusunan nama
print("----MENYUSUN NAMA BERDASARKAN PANJANG KARAKTER----")
banyakSiswa = int(input("Banyaknya siswa :"))

dataMahasiswa = []
i = 0
#mendata nama siswa
while i < banyakSiswa:
    namaMahasiswa = input("Nama Mahasiswa: ")
    i += 1
    dataMahasiswa += [namaMahasiswa]

dataMahasiswa.sort()
i = 0
print("----SUSUNAN NAMA----")
#menentukan jumlah karakter huruf
while i < len(dataMahasiswa):
    print(dataMahasiswa[i], "(", len(dataMahasiswa[i]), "karakter )")
    i += 1