# # mencari waktu saat ini
# import datetime as waktu

# # x = waktu.datetime.now()
# # print(x)

# # # untuk menampilkan tanggal
# # tgl = waktu.date.today()
# # print(tgl)

# # # mengambil tanggal dengan datetime

# # waktuSekarang = waktu.datetime.now()
# # tanggalSekarang = waktuSekarang.strftime("%A, %d %B %Y")
# # print("Waktu dari datetime : ",waktuSekarang)
# # print("Tanggal dari datetime : ",tanggalSekarang)

# # mengubah dari string ke waktu 
# tglLahir = "25/09/2005 18:10"
# ubahKewaktu = waktu.datetime.strptime(tglLahir, "%d/%m/%Y %H:%M")
# print("Default : ",ubahKewaktu)
# print("Setelah diubah : ",ubahKewaktu.strftime("%d/%m/%Y %H:%M"))

# # mencari selisih waktu antara dua tanggal
# # dengan date
# tanggalLahir = waktu.date(2005, 9, 25)
# tglHariIni = waktu.date.today()
# umurSekarang = tglHariIni.year - tanggalLahir.year
# print("umur sekarang adalah",umurSekarang)

# # menggunakan datetime
# tanggalLahir = waktu.datetime(day=25, month=9, year=2005)
# tglHariIni = waktu.datetime.today()
# umurSekarang = tglHariIni.hour - tanggalLahir.hour
# print("jumlah selisih hari ",umurSekarang)

# tambahHari = waktu.timedelta(1000)
# hasilTambah = tglHariIni + tambahHari
# print("Tanggal hari ini ",tglHariIni)
# print("Hasil jumlah hari ",hasilTambah)
# print("Hari yang sudah dijumlahkan adalah hari",hasilTambah.strftime("%A"))




# CHALLENGE
import datetime as dt

list_menu = [
    {"nama": "Mie Goreng", "harga": 10000},
    {"nama": "Nasi Goreng", "harga": 12000},
    {"nama": "Nasi Ayam", "harga": 15000},
    {"nama": "Sate Ayam", "harga": 25000},
    {"nama":"Bakso Setan", "harga": 18000},
]

list_pesanan = []

def menu():
    pesan = 1 
    print("\n")
    for makanan in list_menu:
        print(f"{pesan}. {makanan['nama']} (Rp.{makanan['harga']})")
        pesan += 1

def tambah_pesanan(makanan, jumlah):
    data = {"nama": makanan["nama"], "harga": makanan["harga"], "jumlah": jumlah}
    list_pesanan.append(data)

def hitung_tagihan():
    tagihan = 0

    for pesanan in list_pesanan:
        harga = pesanan["harga"] * pesanan["jumlah"]
        tagihan += harga

    return tagihan

def struk_pesanan(pelanggan, jumlah_bayar):
    tagihan = hitung_tagihan()
    kembalian = jumlah_bayar - tagihan

    print("\n===================================")
    print("         Struk Pembelian")
    print("Nama             : ", pelanggan)
    print("Pesanan          : ")
    for pesanan in list_pesanan:
        print(f"\t      - {pesanan['nama']} (Rp. {pesanan['harga']}) x {pesanan['jumlah']}")
        print("\n")
        print("Tagihan              : Rp.", tagihan)
        print("Jumlah Bayar         : Rp.", jumlah_bayar)
        print("Kembalian            : Rp.",kembalian)
        print("Waktu Pemesanan      : Rp.",dt.datetime.now())
        print("===================================")

while True:
    pelanggan = input("Masukkan nama pelanggan : ")
    while True:
        menu()
        menu_makanan = input("Pilih menu yang akan dipesan atau jika tidak ketik 'selesai' : ")
        if menu_makanan == "selesai":
            break

        jumlah_makanan = int(input("Masukkan jumlah pesanan : "))
        menu_makanan_int = int(menu_makanan)

        if menu_makanan_int > 0 and menu_makanan_int <= len(list_menu):
            tambah_pesanan(list_menu[menu_makanan_int - 1], jumlah_makanan)

        else:
            print("\n=================")
            print("==Menu tidak ada==")
            print("==================")

    jumlah_bayar = int(input("Masukkan jumlah pembayaran : "))
    struk_pesanan(pelanggan, jumlah_bayar)
    list_pesanan = []

    lagi = input("Apakah anda ingin memesan lagi? [Y/T] : ")
    if lagi == "T" or lagi == "t":
        break