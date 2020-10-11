import numpy as np 
A = [45,37,41,35,39]
B = [38,31,26,28,33]
C = [10,15,17,21,12]

data = np.array([A, B, C])
print("Kovarian : \n\n", np.cov(data))
print()
print("Kolerasi : \n\n", np.corrcoef(data))