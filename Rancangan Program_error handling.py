import time
import pandas as pd
selangwaktu = ["Tahunan", "Tengah Tahunan", "Kuartal", "Bulanan"]
saldototal = []
bungatotal = [0]
data_investasi = []
data_investasi2= []
saldo0 = []

def akrualnormal (n):
    x = (1+(sb/n))
    akrualnormal = (saldopokok*(x**(n*lamainvestasi)))
    print("="*50)
    print("Jumlah Akrual\t\t: Rp", akrualnormal)

def akrualbulanan (n):
    x = (1+(sb/n))
    akrualbulanan = (saldopokok*(x**(n*lamainvestasi)))+((kb*(((1+(sb/12))**(12*lamainvestasi))-1))/(sb/12))
    print("="*50)
    print("Jumlah Akrual\t\t: Rp", akrualbulanan)

def perhitungan_normal (n):
    perulangan = 1
    if perulangan == 1:
        bunga1= bungaperiode/n
        saldo1 = float(saldopokok)+bunga1
        bungatotal.append(bunga1)
        saldototal.append(saldo1)
        bungaakhir = bunga1
        perulangan+=1
        data_investasi.append(saldo1)
        data_investasi2.append(bunga1)
    while perulangan<=lamainvestasi*n:
        bunganext=(saldo1*sb)/n
        saldo1=saldo1+bunganext
        saldototal.append(saldo1)
        bungatotal.append(bunganext)
        bungaakhir+=bunganext
        perulangan+=1
        data_investasi.append(saldo1)
        data_investasi2.append(bunganext)
    if perulangan>lamainvestasi*n:
        data1={'Saldo Per Periode' : saldototal, 'Bunga Per Periode' : bungatotal}
        df=pd.DataFrame(data1)
        print(df)
        akrualnormal (n)
        persentase=(bungaakhir/saldopokok)*100
        print("Bunga Akhir Tahun\t: Rp",bungaakhir, "\nPersentase Keuntungan\t: ", persentase, "%")
        print("-"*50)


def perhitungan_bulanan (n):
    perulangan = 1
    setoran = kb*12
    if perulangan == 1:
        bunga2 = (bungaperiode+setoran)/n
        saldo2 = float(saldopokok)+bunga2
        bungatotal.append(bunga2)
        saldototal.append(saldo2)
        bungaakhir2 = bunga2
        perulangan+=1
        data_investasi.append(saldo2)
        data_investasi2.append(bungaakhir2)
    while perulangan <= lamainvestasi*n:
        bunganext2 = ((saldo2*sb)+setoran)/n
        saldo2= saldo2+bunganext2
        saldototal.append(saldo2)
        bungatotal.append(bunganext2)
        bungaakhir2 += bunganext2
        perulangan+=1
        data_investasi.append(saldo2)
        data_investasi2.append(bungaakhir2)
    if perulangan > lamainvestasi*n:
        data1={'Saldo Per Periode' : saldototal, 'Bunga Per Periode' : bungatotal}
        df=pd.DataFrame(data1)
        print(df)
        akrualbulanan (n)
        persentase=(bungaakhir2/saldopokok)*100
        print("Bunga Akhir Tahun\t: Rp",bungaakhir2, "\nPersentase Keuntungan\t: ", persentase, "%")
        print("-"*50)


#login
list_user = ["pticl.pticl123"]

masuk = 1
user = input("Username :")
password = input("Password :")
login = user +"."+password

while masuk!=3 and login not in list_user :
    print("Username atau Password Anda salah. Silahkan login kembali!.")
    masuk += 1
    user = input("Username\t: ")
    password = input("Password\t: ")
    login = user +"."+password
if masuk ==3 and login not in list_user :
    print ("Percobaan login habis. Silahkan coba lagi nanti.")
    quit()

#input data
x = True
while x == True:
    perulangan=1
    while True:
        try:
            saldopokok = float(input("Masukkan Saldo Pokok\t\t: Rp"))
            saldototal.append(saldopokok)
            saldo0.append(saldopokok)
        except:
            print('Harap Masukkan Angka')
            print("")
        else:
            break
    while True:
        try:
            sukubunga = float(input("Masukkan Suku Bunga\t\t: "))
        except:
            print('Harap Masukkan Angka')
            print("")
        else:
            break
    while True:
        try:
            lamainvestasi = int(input("Masukkan Lama Investasi (tahun)\t: "))
        except:
            print('Harap Masukkan Angka')
            print("")
        else:
            break

    #menampilkan selang waktu
    print("\nJenis Selang Waktu: ")
    i=0
    for i, item in enumerate(selangwaktu):
        for key in selangwaktu:
            i+=1
            print(i, key)
        break
    
    #pilih selang waktu
    while True:
        try:
            pilihan = int(input("Pilih selang waktu: "))
        except:
            print('Harap Masukkan Angka 1/2/3/4')
            print("")
        else:
            break
    print("Selang Waktu yang dipilih: ", selangwaktu[pilihan-1], "\n")

    #perhitungan
    b=1
    sb=(float(sukubunga)/100)
    bungaperiode = (float(saldopokok)*sb)
    perhitungan=input("Apakah akan melakukan perhitungan investasi bunga majemuk normal? yes/no: ").lower()
    if perhitungan=="yes":
        print("-"*50)
        print(" "*15, "DATA INVESTASI")
        print("-"*50)
        while pilihan==1:
            perhitungan_normal (1)
            saldototal.clear()
            del bungatotal[1:(lamainvestasi*1)+1]
            print(saldototal, bungatotal)
            break
        while pilihan == 2:
            perhitungan_normal (2)
            break
        while pilihan == 3:
            perhitungan_normal (4)
            break
        while pilihan == 4:
            perhitungan_normal (12)
            break
        perulangan+=1
    else:
        kb=float(input("Masukkan Kontribusi Bulanan: Rp")) 
        print("-"*50)
        print(" "*15, "DATA INVESTASI")
        print("-"*50)
        while pilihan == 1:
            perhitungan_bulanan (1)
            break
        while pilihan == 2:
            perhitungan_bulanan (2)
            break
        while pilihan == 3:
            perhitungan_bulanan (4)
            break
        while pilihan == 4:
            perhitungan_bulanan (12)
            break  
        perulangan+=1
    perhitungan=input("\nApakah akan melakukan perhitungan investasi bunga majemuk lagi? yes/no: ").lower()    
    if perhitungan == "yes":
        x == True
        continue
    else: 
        while perulangan == 1:
           break
        while perulangan > 1:
            output=input("Ingin Tampilkan Data Kumulatif? (yes/no): ").lower()
            if output == "yes":
                print("-"*50)
                print(" "*12, "DATA KUMULATIF INVESTASI")
                print("-"*50)
                data={'Saldo Per Periode' : data_investasi, 'Bunga Per Periode' : data_investasi2}
                df=pd.DataFrame(data)
                print (df)
                print("-"*50)
                print("Saldo Total\t\t: Rp",sum(saldototal),"\nBunga Total\t\t: Rp",sum(bungatotal))
                break
            else:
                break
    Localtime = time.asctime(time.localtime(time.time()))
    print("-"*50)
    print("Diakses oleh\t: ", user, "\nWaktu akses\t: ", Localtime)
    print("-"*50, "\n", " "*20,"SELESAI")
    print("-"*50)
    quit()