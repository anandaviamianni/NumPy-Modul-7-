import numpy as np 
bilangan= [69, 79, 67, 64, 83, 66, 58, 81, 69, 60, 60, 66, 50, 67, 63, 78, 61, 63, 70, 60]
mean = np.mean(bilangan)
print("Mean : ",mean)

minimal = np.min(bilangan)
maksimal = np.max(bilangan)
nilaitengah = np.median(bilangan)
print("Nilai Minimal = ",minimal)
print("Nilai Maksimal = ", maksimal)
print("Nilai Tengah = ", nilaitengah)

st_dev = np.std(bilangan)
print("Standar Deviasi = ", round(st_dev, 2))

variasi = np.var(bilangan)
print("Variasi Bilangan = ", variasi)