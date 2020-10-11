Databeras = [14000, 12500, 13000, 10000, 11000, 11000, 9750]
Datakunjungan = [500, 400, 300, 340, 557, 200, 900]


def mean(Databeras):
    sum = 0
    for i in Databeras:
        sum += i
    return sum/len(Databeras)

Databeras.sort()
if len(Databeras) % 2 == 0:
    rumus = int(len(Databeras)/ 2)
    median = (Databeras[rumus - 1] + Databeras[rumus] / 2)
else:
    rumus = int((len(Databeras)+ 1) / 2)
    median = Databeras[rumus - 1]

def modus (x = []):
    anggota = set(x)
    mode = []
    highestTotal = 0
    for a in anggota:
        jumlah = x.count(a)
        if( jumlah>1 and jumlah>highestTotal):
            mode.clear()
            highestTotal = jumlah
            mode.append(a)
        elif(jumlah == highestTotal):
            mode.append(a)
    return mode

databeras = [14000, 12500, 13000, 10000, 11000, 11000, 9750]
import numpy as np 
st_dev = np.std(databeras)
Q1 = np.quantile(databeras, 0.25)
Q2 = np.quantile(databeras, 0.5)
Q3 = np.quantile(databeras, 0.75)
data = np.array([Databeras,Datakunjungan])
kovarian = np.cov(data)
korelasi = np.corrcoef(data)

import statistics as st 
modus= st.multimode(Databeras)

print("="*20,"Menghitung Harga Beras","="*20 )
print("Data Harga Beras\t\t\t                      :",databeras)
print("Data Kunjungan Harian \t\t\t\t              :",Datakunjungan)
print("Mean Harga Beras\t\t\t                      : RP", mean(Databeras))
print("Median Harga Beras\t\t\t                      : RP", median)
print("Modus Harga Beras\t\t\t                      : RP", modus)
print("Standar Deviasi Harga Beras\t\t\t              :", round(st_dev,2))
print("Kuartil 1 Harga Beras\t\t\t                      : RP", Q1)
print("Kuartil 2 Harga Beras\t\t\t                      : RP", Q2)
print("Kuartil 3 Harga Beras\t\t\t                      : RP", Q3)
print("Kovarian Harga Beras dengan Jumah Kunjungan\t\t      : ")
print(np.cov(data))
print("Korelasi Harga Beras dengan Jumah Kunjungan\t\t      : ")
print(np.corrcoef(data))