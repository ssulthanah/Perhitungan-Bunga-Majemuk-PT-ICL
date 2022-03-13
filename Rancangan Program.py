selangwaktu = ["Tahunan", "Tengah Tahunan", "Kuartal", "Bulanan"]

#input data
saldopokok = float(input("Masukkan Saldo Pokok: Rp"))
sukubunga = float(input("Masukkan Suku Bunga: "))
lamainvestasi = int(input("Masukkan Lama Investasi (tahun): "))

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

#perhitungan majemuk normal dan kontribusi bulanan
bungaperiode = saldopokok*sukubunga
saldoperiode = saldopokok+bungaperiode
perhitungan=input("Apakah akan melakukan perhitungan investasi bunga majemuk normal? yes/no: ").lower()
if perhitungan=="yes":
    if pilihan==1:
        bunga1= bungaperiode
        saldo1 = saldopokok+bunga1
        akrualnormal = (saldopokok*((1+sukubunga/1)**(1*lamainvestasi)))
    elif pilihan==2 :
        bunga1 = bungaperiode/2
        saldo1 = saldopokok+bunga1
        akrualnormal = (saldopokok*((1+sukubunga/2)**(2*lamainvestasi)))
    elif pilihan==3 :
        bunga1 = bungaperiode/4 
        saldo1 = saldopokok+bunga1
        akrualnormal = (saldopokok*((1+sukubunga/4)**(4*lamainvestasi)))
    elif pilihan==4 :
        bunga1 = bungaperiode/12 
        saldo1 = saldopokok+bunga1
        akrualnormal = (saldopokok*((1+sukubunga/12)**(12*lamainvestasi)))
    print("Bunga Per Periode\t: Rp", bungaperiode, "\nSaldo Per Periode\t: Rp", saldoperiode, "\nJumlah Akrual Normal\t: Rp", akrualnormal)      
else:
    kb=float(input("Masukkan Kontribusi Bulanan: Rp"))
    if pilihan == 1:
        bunga2 = bungaperiode+kb
        saldo2 = saldopokok+bunga2
        akrualbulanan = (saldopokok*((1+sukubunga/1)**(1*lamainvestasi)))+(((kb+(1+sukubunga/1))**(1*lamainvestasi))-1)/(sukubunga/1)
    elif pilihan == 2 :
        bunga2 = (bungaperiode/2)+kb
        saldo2 = saldopokok+bunga2
        akrualbulanan = (saldopokok*((1+sukubunga/2)**(2*lamainvestasi)))+(((kb+(1+sukubunga/2))**(2*lamainvestasi))-1)/(sukubunga/2)
    elif pilihan == 3 :
        bunga2 = (bungaperiode/4)+kb
        saldo2 = saldopokok+bunga2
        akrualbulanan = (saldopokok*((1+sukubunga/4)**(4*lamainvestasi)))+(((kb+(1+sukubunga/4))**(4*lamainvestasi))-1)/(sukubunga/4)
    elif pilihan == 4 :
        bunga2 = (bungaperiode/12)+kb
        saldo2 = saldopokok+bunga2
        akrualbulanan = (saldopokok*((1+sukubunga/12)**(12*lamainvestasi)))+(((kb+(1+sukubunga/12))**(12*lamainvestasi))-1)/(sukubunga/12)
    print("Bunga Per Periode\t: Rp", bunga2, "\nSaldo Per Periode\t: Rp", saldo2, "\nJumlah Akrual dengan Kontribusi Bulanan: Rp", akrualbulanan)

    

   
#bunga_akhirtahun1 = bungaperiode
