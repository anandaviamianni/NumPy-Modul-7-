ls = [1,1,1,2,2,3,4,1,2,2,3,1,2]
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
print("Modusnya adalah: ",modus(ls))