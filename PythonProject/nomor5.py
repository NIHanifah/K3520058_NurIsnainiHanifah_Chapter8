#membuat kudrat dari list
print("----KUADRAT DARI LIST----")

#function utnuk pengkuadratan
def kuadrat(bil):
    hasilKuadrat =[]
    i = 0
    while i < len(bil):
        kuadrat = bil[i] ** 2
        hasilKuadrat += [kuadrat]
        i += 1
    print("hasil kuadrat bil = ", hasilKuadrat)


bil = [2, 4, 5, 6]
print("bil =", bil)
kuadrat(bil)