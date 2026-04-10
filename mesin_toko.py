import json

def simpan_database(daftar_nama,list_total):
    data_warung = {
        "statistik": {
            "jumlah_pembeli": len(daftar_nama),
            "total_uang": sum(list_total)
        },
        "daftar_pelanggan":daftar_nama,
        "daftar_tagihan":list_total
    }
    
    with open ("database_warung.json", "w") as file:
        json.dump(data_warung,file,indent=4)
    print(">> DATA BERHASIL DI-BACKUP KE SISTEM DATABASE JSON <<")    


def cetak_struk(nama_pembeli, total_bayar):
    print(f"{' STRUK BELANJA ' :=^30}")
    print(f"{' Nama Pelanggan ' :<30} : {nama_pembeli}")
    print(f"{' Total yang harus dibayar ' :<30} : Rp {total_bayar}")
    print("=" * 30 )
    
def simpan_laporan(daftar_nama,list_total):
    with open ("laporan_hari_ini.txt","w") as teks:
        teks.write(f"{'LAPORAN PENJUALAN' :=^35}\n\n")
        
        jumlah_orang={len(daftar_nama)}
        uang_masuk={sum(list_total)}
        
        teks.write(f"{'Jumlah Pembeli Hari Ini  ' :<30}: {jumlah_orang} orang \n")
        teks.write(f"{'Total Uang Masuk Hari Ini ':<30}: Rp {uang_masuk}\n\n")
        
        teks.write("Daftar Pelanggan:\n")
        for nomor,nama in enumerate (daftar_nama,start=1):
            teks.write(f"{nomor}. {nama}\n")
    print(">> Laporan berhasil disimpan ke file 'laporan_warung.txt' <<")  