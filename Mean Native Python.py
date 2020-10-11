# Menggunakan Native Python
data = [1,1,1,1,2,2,2,2,2,3]
def mean(data):
    sum = 0
    for i in data:
        sum += i
    return sum/len(data)

print("Mean: ", mean(data))

