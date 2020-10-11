Databeras = [14000, 12500, 13000, 10000, 11000, 11000, 9750] #Membuat list Data Beras
Datakunjungan = [500, 400, 300, 340, 557, 200, 900] #Membuat list Data Beras

class modusmeanmedian(): #membuat sebuah deklarasi kelas
    def __init__ (self, Databeras, Datakunjungan): #mendefinisikan suatu fungsi dengan self, data beras dan data kunjungan
        #memasukkan isi dari data beras dan kunjungan ke variabel self
        self.Databeras = Databeras
        self.Datakunjungan = Datakunjungan
    def mean(self): # Membuat fungsi mean dengan parameter self
        sum = 0 #Digunakan untuk menjumlahkan semua bilangan data
        for i in self.Databeras: #menggunakan perulangan for dalam menjumlahkan data
            sum += i
        return sum/len(self.Databeras) #fungsi akan mengembalikan jumlah data yang telah dihitung dan hasilnya dibagi dengan banyaknya index data beras 
    
    def median(self): #membuat fungsi median dengan parameter self
        self.Databeras.sort() # untuk mencari median kita harus menyusun data beras dari kecil hingga terbesar menggunakan sort()
        if len(self.Databeras) % 2 == 0: #kondisi if jika panjang data beras dimoduluskan menghasilkan hasil 0
            rumus = int(len(Databeras)/ 2) #jika kondisi if maka data akan dimasukkan ke dalam rumus yaitu banyaknya index data dibagi 2 dan menghasilkan bilangan integer
            median = (Databeras[rumus - 1] + Databeras[rumus] / 2) #hasil dari rumus akan dimasukkan kedalam hasil dari variabel median dengan rumus median yg baru
            return median #fungsi akan mengembalikan jumlah ke median
        else:
            rumus = int((len(Databeras)+ 1) / 2) #jika kondisi else terpenuhi maka program automatis memasukkan banyaknya index ke dalam rumus yang telah disediakan
            median = Databeras[rumus - 1] #hasil rumus dimasukkan ke dalam variabel  median dengan rumus variabel yang baru
            return median #fungsi akan mengembalikan hasil ke median
            #untuk hal ini program mendeteksi bahwa banyaknya index jika di moduluskan tidak menghasilkan 0 maka kondisi yang dipake adalah kondisi else.
    
    def modus(self): # membuat fungsi modus dengan parameter self
        isilist = self.Databeras #program akan memasukan list databeras ke dalam variabel isi list
        listmodus=[] # membuat list kosong untuk memasukkan nilai modus
        nilaitertinggi = 0 #membuat variabel baru untuk menyimpan nilai tertinggi pada data beras
        for a in isilist: #menggunakan perulangan for dengan banyaknya a di dalam isilist yang hasilnya 4
            jumlah = self.Databeras.count(a) #di dalam variabel jumlah ini program akan mengitung jumlah data 
            #menggunakan kondisi if elif
            if(jumlah>1 and jumlah>nilaitertinggi): #kondisi if jika hasil jumlah lebih besar dari 1 dan hasil jumlah lebih besar dari hasil nilaitertinggi
                #jika kondisi if terpenuhi maka program akan menghapus listmodus yang telah kita buat
                listmodus.clear()
                # hasil nilai tertinggi akan masuk ke dalam variabel jumlah
                nilaitertinggi=jumlah
                # menambahkan hasil a kedalam listmodus yang telah dihapus sebelumnya
                listmodus.append(a)
        return listmodus #mengembalikan hasil ke listmodus

    def standardev(self):#membuat fungsi standar deviasi 
        import numpy as np #mengimport library numpy dan menjadikannya np
        databe = self.Databeras #memasukkan isi dari data beras ke dalam variabel baru
        stadev = np.std(databe) #untuk mencari standar deviasi bisa digunakan np.std(# variabel data yang ingin dihitung)
        return round(stadev,2) #mengembalikan fungsi dengan menggunakan round dan diakhiri 2 untuk mengambil 2 angka di belakang koma

    def q1(self): #membuat fungsi kuartil 1
        import numpy as np #mengimport library numpy dan menjadikannya np
        databe = self.Databeras #memasukkan isi dari data beras ke dalam variabel baru
        Q1 = np.quantile(databe, 0.25) #untuk mencari kuartil  bisa digunakan np.quantile(# variabel data yang ingin dihitung, rumus kuartil 1)
        return Q1 #mengembalikan fungsi kuartil 1

    def q2(self): #membuat fungsi kuartil 2
        import numpy as np #mengimport library numpy dan menjadikannya np
        databe = self.Databeras #memasukkan isi dari data beras ke dalam variabel baru
        Q2 = np.quantile(databe, 0.5)  #untuk mencari kuartil  bisa digunakan np.quantile(# variabel data yang ingin dihitung, rumus kuartil 2)
        return Q2 #mengembalikan fungsi kuartil 2

    def q3(self): #membuat fungsi kuartil 3
        import numpy as np #mengimport library numpy dan menjadikannya np
        databe = self.Databeras #memasukkan isi dari data beras ke dalam variabel baru
        Q3 = np.quantile(databe, 0.75) #untuk mencari kuartil  bisa digunakan np.quantile(# variabel data yang ingin dihitung, rumus kuartil 3)
        return Q3 #mengembalikan fungsi kuartil 3

    def kovari(self): #membuat fungsi kovari
        import numpy as np #mengimport library numpy
        databe = self.Databeras #memasukkan isi dari data beras ke dalam variabel baru
        dataku = self.Datakunjungan #memasukkan isi dari data kunjungan ke dalam variabel baru
        darray = np.array([databe,dataku]) #untuk mencarikovarian  kita dapat memakai np.array(Data yang ingin dihasilkan 1, data yang ingin dihasilkan 2) dan memasukkannya kedalam list untuk menghasilkan array
        kovarian = np.cov(darray) #memasukkan hasil array covarian ke dalam variabel baru
        return kovarian #mengembalikan fungsi kovarian

    def korela(self): #membuat fungsi kolera
        import numpy as np #mengimport library numpy
        databe = self.Databeras #memasukkan isi dari data beras ke dalam variabel baru
        dataku = self.Datakunjungan #memasukkan isi dari data kunjungan ke dalam variabel baru
        darray = np.array([databe,dataku]) #untuk mencari kolerasi  kita dapat memakai np.array(Data yang ingin dihasilkan 1, data yang ingin dihasilkan 2) dan memasukkannya kedalam list untuk menghasilkan array
        korelasi = np.corrcoef(darray) #memasukkan hasil array korelasi ke dalam variabel baru
        return korelasi  #mengembalikan fungsi korelasi
        
    def cetak(self): #mencetak hasil data
        print("="*20,"Menghitung Harga Beras","="*20 )
        print("Data Harga Beras\t\t\t                      :",self.Databeras)
        print("Data Kunjungan Harian \t\t\t\t              :",self.Datakunjungan)
        print("Mean Harga Beras\t\t\t                      : RP", self.mean())
        print("Median Harga Beras\t\t\t                      : RP", self.median())
        print("Modus Harga Beras\t\t\t                      : RP", self.modus())
        print("Standar Deviasi Harga Beras\t\t\t              :", self.standardev())
        print("Kuartil 1 Harga Beras\t\t\t                      : RP", self.q1())
        print("Kuartil 2 Harga Beras\t\t\t                      : RP", self.q2())
        print("Kuartil 3 Harga Beras\t\t\t                      : RP", self.q3())
        print("Kovarian Harga Beras dengan Jumah Kunjungan\t\t      : ")
        print(self.kovari())
        print("Korelasi Harga Beras dengan Jumah Kunjungan\t\t      : ")
        print(self.korela())
#memanggil keluar program untuk mencetak hasil data
data = modusmeanmedian(Databeras,Datakunjungan)
data.cetak()