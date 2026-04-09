semua_pembeli = []
semua_total = []
katalog = {
    "Kopi" : 5000,
    "Indomie" : 7500,
    "Nutrisari" : 5000
}

def cetak_struk(nama_pembeli, total_bayar):
    print("=====STRUK BELANJA====")
    print("Nama Pelanggan : " + nama_pembeli)
    print(f"Total yang harus dibayar : Rp {total_bayar}")
    print("======================")
    
def simpan_laporan(daftar_nama,list_total):
    with open ("laporan_hari_ini.txt","w") as teks:
        teks.write("====Laporan Penjualan Hari Ini====\n")
        
        jumlah_orang={len(daftar_nama)}
        uang_masuk={sum(list_total)}
        
        teks.write(f"Jumlah Pembeli Hari Ini : {jumlah_orang}\n")
        teks.write(f"Total Uang Masuk Hari Ini : Rp {uang_masuk}\n")
        
        teks.write("Daftar Pelanggan:\n")
        for nama in daftar_nama:
            teks.write(f"- {nama}\n")
    print(">> Laporan berhasil disimpan ke file 'laporan_warung.txt' <<")         

lagi="y"
while lagi == "y":
    print("TOKO CIJEN")
    nama=input("siapa nama kamu ? ")
    beli_barang=(input("Mau beli apa ? (Kopi/Indomie/Nutrisari) : "))
    while beli_barang not in katalog:
        print("Maaf barang tersebut tidak ada, coba perbaiki ketikanmu!")
        beli_barang=(input("Mau beli apa ? (Kopi/Indomie/Nutrisari) : "))
    jumlah_barang=int(input("berapa jumlah barang yang kamu beli ? "))
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