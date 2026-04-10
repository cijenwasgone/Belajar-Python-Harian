import hashlib
import time  #untuk memberi jeda waktu

#ini alat untuk menyerang website, brute force yaitu menyerang website/bagian admin dengan cara menebak password
# hash yang dicuri dari admin_warung.py 
TARGET_HASH = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"

print("=== [ SYSTEM BREACH INITIATED ] ===")
print("Memulai serangan Brute Force...\n")

# 1. membuka file kumpulan password
with open("wordlist.txt", "r") as file:
    # membaca isi file tersebut, satu per satu dan membuang karakter spasi/enter
    daftar_tebakan = file.read().splitlines()

password_ditemukan = False

# 2. Mesin Pengecek Otomatis (Looping)
for tebakan in daftar_tebakan:
    print(f"[*] Mencoba password: {tebakan} ...")
    time.sleep(0.5) # Jeda saat menebak password, agar terlihat password apa saja yang dicoba
    
    # mengubah password tebakan menjadi hash
    hash_tebakan = hashlib.sha256(tebakan.encode()).hexdigest()
    
    # 3. Mencocokan hash tebakan dengan target hash
    if hash_tebakan == TARGET_HASH:
        print("\n" + "="*40)
        print("[!!!] PASSWORD BERHASIL DI TEMUKAN [!!!]")
        print(f"Password aslinya adalah : >> {tebakan} <<")
        print("="*40)
        password_ditemukan = True
        break # menghentikan program ketika password sudah diketahui

# Jika loop selesai tapi tidak ketemu/ tidak ada yang sama
if not password_ditemukan:
    print("\n[-] Misi Gagal. Password tidak ada di dalam wordlist.")