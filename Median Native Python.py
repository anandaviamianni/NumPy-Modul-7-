KumpulanAngka = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
KumpulanAngka.sort()

if len(KumpulanAngka) % 2 == 0:
    rumus = int(len(KumpulanAngka)/ 2)
    median = (KumpulanAngka[rumus - 1] + KumpulanAngka[rumus] / 2)
else:
    rumus = int((len(KumpulanAngka)+ 1) / 2)
    median = KumpulanAngka[rumus - 1]

print("Median data adalah ", median)


