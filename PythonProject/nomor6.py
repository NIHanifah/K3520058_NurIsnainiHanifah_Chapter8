#mengurutkan data berdasarkan panjang karakter
print("----MNEGURUTKAN DATA BERDASARKAN PANJANG KARAKTER----")

#function untuk mengurutkan
def sortStringByChar(myData):
    myData.sort(key = len, reverse = True)
    print("Urutan data : ", myData)

myData = ['apel', 'rambutan', 'jeruk']
print("Data : ", myData)
sortStringByChar(myData)