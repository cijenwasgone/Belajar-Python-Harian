import json
import hashlib
import getpass

#admin123 password ini sudah disamarkan menjadi hash
print("=== PORTAL ADMIN RAHASIA ===")

#hash untuk menyamarkan password
HASH_BENAR = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"

#fungsi getpass untuk menyembunyikan teks di bagian memasukan password
tebakan_user = getpass.getpass("Masukkan Password: ")

#berfungsi untuk mengubah password yang diberikan user menjadi hash
hash_tebakan = hashlib.sha256(tebakan_user.encode()).hexdigest()

#membandingkan hash dengan hash
if hash_tebakan == HASH_BENAR:
    print("\n[+] AKSES DITERIMA! Sedang menyedot data...")
    print("-" * 35)
    
    
    with open("database_warung.json", "r") as file:
        data_rahasia = json.load(file)

    uang_terkumpul = data_rahasia["statistik"]["total_uang"]
    jumlah_tamu = data_rahasia["statistik"]["jumlah_pembeli"]

    print(f"Lapor Bos Cijen! Hari ini kita dapat uang: Rp {uang_terkumpul}")
    print(f"Total ada {jumlah_tamu} orang yang datang.")

    print("\nDaftar Pelanggan:")
    for nomor, nama in enumerate(data_rahasia["daftar_pelanggan"], start=1):
        print(f"{nomor}. {nama}")


else:
    # output Jika hash tidak cocok
    print("\n[!] AKSES DITOLAK! Sistem akan terkunci otomatis.")