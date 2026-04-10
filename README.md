# 🛒 Warung Cijen - Aplikasi Kasir Modular

> Proyek pembelajaran Python (Hari 1-3) yang berfokus pada logika pemrograman, *file handling*, arsitektur perangkat lunak, dan pengenalan keamanan siber dasar.

## 📌 Fitur Utama
Aplikasi ini bukan sekadar program kasir biasa, melainkan sudah dilengkapi dengan standar industri:
- **Tahan Banting (Error Handling):** Menggunakan `try...except` agar aplikasi tidak *crash* saat pengguna memasukkan tipe data yang salah.
- **Arsitektur Modular:** Kode tidak menumpuk di satu tempat. Dipisah menjadi file katalog, mesin fungsi, dan program utama.
- **Database JSON:** Data transaksi (nama pembeli dan total belanja) diekspor secara rapi ke format standar `.json`.
- **Keamanan Kriptografi (Blue Team):** Dilengkapi dengan Dashboard Admin rahasia yang dilindungi oleh sistem *login* berbasis **SHA-256 Hashing**.
- **Simulasi Serangan (Red Team):** Terdapat skrip `brute_force.py` untuk menguji kerentanan *password* menggunakan *Dictionary Attack*.

## 📂 Struktur Direktori
- `warung.py` : Program utama (Front-End) untuk melayani pembeli.
- `katalog_toko.py` : Ruang penyimpanan data (katalog harga barang).
- `mesin_toko.py` : Mesin pemroses (cetak struk rapi dengan f-string & ekspor JSON).
- `admin_warung.py` : Portal *Back-End* untuk membaca database `.json` (Butuh *password*).
- `brute_force.py` : Skrip otomatis penyerang untuk mensimulasikan *hacking password*.
- `.gitignore` : Penjaga rahasia agar file database asli tidak bocor ke publik.
