import numpy as np 
KumpulanAngka = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

Q1 = np.quantile(KumpulanAngka, 0.25)
Q2 = np.quantile(KumpulanAngka, 0.5)
Q3 = np.quantile(KumpulanAngka, 0.75)

print("Kuartil 1 (Q1) :", Q1)
print("Kuartil 2 (Q2) :", Q2)
print("Kuartil 3 (Q3) :", Q3)
