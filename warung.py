from katalog_toko import katalog
from mesin_toko import cetak_struk,simpan_laporan,simpan_database

semua_pembeli = []
semua_total = []

lagi="y"
while lagi == "y":
    print("TOKO CIJEN")
    nama=input("siapa nama kamu ? ")
    beli_barang=(input("Mau beli apa ? (Kopi/Indomie/Nutrisari) : "))
    while beli_barang not in katalog:
        print("Maaf barang tersebut tidak ada, coba perbaiki ketikanmu!")
        beli_barang=(input("Mau beli apa ? (Kopi/Indomie/Nutrisari) : "))
    while True:
        try:
            jumlah_barang=int(input("berapa jumlah barang yang kamu beli ? "))
            break
        except ValueError:
            print("Waduh, masukan angka saja, jangan huruf")
    harga_barang=katalog[beli_barang]
    total_harga=harga_barang*jumlah_barang

    if total_harga > 100000:
        print("selamat kamu mendapatkan diskon 10%")
        total_harga = total_harga - (total_harga * 0.1) 
    else: 
        print("maaf kamu tidak mendapatkan diskon")
        
    semua_pembeli.append(nama)    
    semua_total.append(total_harga)    
    cetak_struk(nama,total_harga)    
    lagi = input("mau belanja lagi ? (y/n): ")

print("toko ditutup,terimakasih!")
simpan_laporan(semua_pembeli, semua_total)
simpan_database(semua_pembeli,semua_total)