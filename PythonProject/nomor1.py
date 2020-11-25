#Program input data sebanyak n buah
print("----PROGRAM INPUT DATA----")
#input data
banyakNilai = int(input("Banyaknya data :"))

dataNilai = []
i = 0
while i < banyakNilai:
    data = int(input("Masukkan nilai :"))
    i += 1
    dataNilai += [data]

#mengurutkan nilai dari dari besar ke kecil
dataNilai.sort(reverse=True)
print("Urutan nilai =", dataNilai)