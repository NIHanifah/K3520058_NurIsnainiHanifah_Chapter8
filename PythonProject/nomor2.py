#PROGRAM MEMBUAT LIST DARI RERATA, MIN, DAN MAKS
print("----PROGRAM MEMBUAT LIST DARI RERATA, MIN, DAN MAKS----")
#function mencari max, min, dan rerata
def dataStat(x):
    rerata = sum(x) / len(x)
    data = []
    data.append(int(rerata))
    data.append(max(x))
    data.append(min(x))
    print("List dari hasil rerata, max, dan min : ", data)


x = [3, 4, 1, 5, 2]
print("List pertama : ", x)
dataStat(x)
