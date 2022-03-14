selangwaktu = ["Tahunan", "Tengah Tahunan", "Kuartal", "Bulanan"]

def akrualnormal (n):
    x = (1+(sukubunga/n))
    akrualnormal = (saldopokok*(x**(n*lamainvestasi)))
    print("="*50)
    print("Jumlah Akrual Normal\t: Rp", akrualnormal)

def akrualbulanan (n):
    x = (1+(sukubunga/n))
    akrualbulanan = (saldopokok*(x**(n*lamainvestasi)))+(((kb*(x**(n*lamainvestasi)))-1)/(sukubunga/n))
    print("="*50)
    print("Jumlah Akrual dengan Kontribusi Bulanan: Rp. ", akrualbulanan)

#input data
x = True
while x == True:
    saldopokok = float(input("Masukkan Saldo Pokok\t\t: Rp"))
    sukubunga = float(input("Masukkan Suku Bunga\t\t: "))
    lamainvestasi = int(input("Masukkan Lama Investasi (tahun)\t: "))

    #menampilkan selang waktu
    print("\nJenis Selang Waktu: ")
    i=0
    for i, item in enumerate(selangwaktu):
        for key in selangwaktu:
            i+=1
            print(i, key)
        break
    
    #pilih selang waktu
    pilihan = int(input("Pilih selang waktu: "))
    print("Selang Waktu yang diplih: ", selangwaktu[pilihan-1], "\n")
    b=1

    #perhitungan majemuk normal dan kontribusi bulanan
    bungaperiode = saldopokok*sukubunga
    saldoperiode = saldopokok+bungaperiode
    perhitungan=input("Apakah akan melakukan perhitungan investasi bunga majemuk normal? yes/no: ").lower()
    if perhitungan=="yes":
        print("-"*50)
        print(" "*15, "DATA INVESTASI")
        print("-"*50)
        while pilihan==1:
            perulangan = 1
            if perulangan == 1:
                bunga1= bungaperiode
                saldo1 = saldopokok+bunga1
                print("Bunga Periode", b, "\t: Rp", bunga1, "\nSaldo Periode", b, "\t: Rp", saldo1)
                bungaakhir = bunga1
                perulangan+=1
            while perulangan<=lamainvestasi:
                bunganext=saldo1*sukubunga
                saldo1=saldo1+bunganext
                b+=1
                print("Bunga Periode", b, "\t: Rp", bunganext, "\nSaldo Periode", b, "\t: Rp", saldo1)
                bungaakhir+=bunganext
                perulangan+=1
            if perulangan>lamainvestasi:
                akrualnormal (1)
                print("Bunga Akhir Tahun\t: Rp",bungaakhir)
                quit()
        while pilihan == 2:
            perulangan=1
            if perulangan == 1:
                bunga1= bungaperiode/2
                saldo1 = saldopokok+bunga1
                print("Bunga Periode", b, "\t: Rp", bunga1, "\nSaldo Periode", b, "\t: Rp", saldo1)
                bungaakhir = bunga1
                perulangan+=1
            while perulangan<=lamainvestasi*2:
                bunganext=(saldo1*sukubunga)/2
                saldo1=saldo1+bunganext
                b+=1
                print("Bunga Periode", b, "\t: Rp", bunganext, "\nSaldo Periode", b, "\t: Rp", saldo1)
                bungaakhir+=bunganext
                perulangan+=1
            if perulangan>lamainvestasi*2:
                akrualnormal (2)
                print("Bunga Akhir Tahun\t: Rp",bungaakhir)
                quit()
        while pilihan == 3:
            perulangan=1
            if perulangan == 1:
                bunga1= bungaperiode/4
                saldo1 = saldopokok+bunga1
                print("Bunga Periode", b, "\t: Rp", bunga1, "\nSaldo Periode", b, "\t: Rp", saldo1)
                bungaakhir = bunga1
                perulangan+=1
            while perulangan<=lamainvestasi*4:
                bunganext=(saldo1*sukubunga)/4
                saldo1=saldo1+bunganext
                b+=1
                print("Bunga Periode", b, "\t: Rp", bunganext, "\nSaldo Periode", b, "\t: Rp", saldo1)
                bungaakhir+=bunganext
                perulangan+=1
            if perulangan>lamainvestasi*4:
                akrualnormal (4)
                print("Bunga Akhir Tahun\t: Rp",bungaakhir)
                quit()
        while pilihan == 4:
            perulangan=1
            if perulangan == 1:
                bunga1= bungaperiode/12
                saldo1 = saldopokok+bunga1
                print("Bunga Periode", b, "\t: Rp", bunga1, "\nSaldo Periode", b, "\t: Rp", saldo1)
                bungaakhir = bunga1
                perulangan+=1
            while perulangan<=lamainvestasi*12:
                bunganext=(saldo1*sukubunga)/12
                saldo1=saldo1+bunganext
                b+=1
                print("Bunga Periode", b, "\t: Rp", bunganext, "\nSaldo Periode", b, "\t: Rp", saldo1)
                bungaakhir+=bunganext
                perulangan+=1
            if perulangan>lamainvestasi*12:
                akrualnormal (12)
                print("Bunga Akhir Tahun\t: Rp",bungaakhir)
                quit()
    elif perhitungan == "no":
        kb=float(input("Masukkan Kontribusi Bulanan: Rp"))
        print("-"*50)
        print(" "*15, "DATA INVESTASI")
        print("-"*50)
        setoran = kb*12
        while pilihan == 1:
            perulangan = 1
            if perulangan == 1:
                bunga2 = bungaperiode+setoran
                saldo2 = saldopokok+bunga2
                print("Bunga Periode", b, "\t: Rp", bunga2, "\nSaldo Periode", b, "\t: Rp", saldo2)
                bungaakhir2 = bunga2
                perulangan+=1
            while perulangan <= lamainvestasi:
                bunganext2 = (saldo2*sukubunga)+setoran
                saldo2= saldo2+bunganext2
                b+=1
                print("Bunga Periode", b, "\t: Rp", bunganext2, "\nSaldo Periode", b, "\t: Rp", saldo2)
                bungaakhir2 += bunganext2
                perulangan+=1
            if perulangan > lamainvestasi:
                akrualbulanan (1) #YANG INI HASILNYA BELOM SESUAI
                quit()

       

#akrualbulanan = (saldopokok*((1+sukubunga/1)**(1*lamainvestasi)))+(((kb+(1+sukubunga/1))**(1*lamainvestasi))-1)/(sukubunga/1)