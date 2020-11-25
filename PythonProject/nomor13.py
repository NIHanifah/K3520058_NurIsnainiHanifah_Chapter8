nilaiMhs = [
    {'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
    {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
    {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
    {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40},
]

def hitungNilaiAkhir():
    dataNilaiAkhir = []
    i = 0
    while i < len(nilaiMhs):
        nilaiAkhir = (nilaiMhs[i]['mid'] * 2 * nilaiMhs[i]['uas']) / 3
        dataNilaiAkhir += [nilaiAkhir]
        nilaiMhs[i]['na'] = nilaiAkhir
        i += 1
    for key in nilaiMhs:
        print(key)

hitungNilaiAkhir()

nilai = [x['na'] for x in nilaiMhs]
max(nilai)
i = 0
while i < len(nilaiMhs):
    if max(nilai) == nilaiMhs[i]['na']:
        print("Nilai Akhir Tertinggi:", nilaiMhs[i]['nama'])
    i += 1
