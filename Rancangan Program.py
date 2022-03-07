
selangwaktu = [{"Tahunan" : 12}, {"Tengah Tahunan" : 6}, {"Kuartal" : 3}, {"Bulanan" : 1}]

#input data
saldopokok = int(input("Masukkan Saldo Pokok: "))
sukubunga = float(input("Masukkan Suku Bunga: "))
lamainvestasi = int(input("Masukkan Lama Investasi (tahun): "))
#menampilkan selang waktu
print("\nJenis Selang Waktu: ")
i=0
for i, item in enumerate(selangwaktu, start=1):
    for key, value in item.items():
        print(i, key, ":", value, "bulan")
    i+=1
#pilih selang waktu
pilihan = int(input("Pilih Selang Waktu: "))
for key, value in selangwaktu[pilihan-1].items():
    print("Selang Waktu yang diplih: ", key, "\n")
#menghitung saldo investasi majemuk normal
bungaperiode = saldopokok*sukubunga
saldoperiode = saldopokok+bungaperiode
print("Jumlah Bunga per Periode: \n", bungaperiode, "Jumlah Saldo per Periode: ", saldoperiode)










