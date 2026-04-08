lagi="y"
while lagi == "y":
    print("TOKO CIJEN")
    nama=input("siapa nama kamu ? ")
    harga_barang=int(input("berapa harga barang yang kamu beli ? "))
    jumlah_barang=int(input("berapa jumlah barang yang kamu beli ? "))
    total_harga=harga_barang*jumlah_barang

    if total_harga > 100000:
        print("selamat kamu mendapatkan diskon 10%")
        total_harga = total_harga - (total_harga * 0.1) 
    else: 
        print("maaf kamu tidak mendapatkan diskon")
        
    print("=====STRUK BELANJA====")
    print("Nama Pelanggan " + nama)
    print(f"Total yang harus dibayar : Rp {total_harga}")
    print("======================")
    lagi = input("mau belanja lagi ? (y/n): ")
    
print("toko ditutup,terimakasih!")