# main.py
from inventaris_pkg.fileio import FileHandler
from inventaris_pkg.processing import Produk, OlahInventaris
from inventaris_pkg.validasi import DataError


def main():
    handler = FileHandler("data_toko.csv")
    handler.inisialisasi_file()

    calon = [
        ("P01", "Monitor", 2000000, 10, "Elektronik"),
        ("P02", "Headset", 300000, 3, "Audio"),
        ("P03", "Mouse", 150000, 2, "Aksesoris"),
        ("P04", "Laptop", 8000000, 5, "Elektronik"),
    ]

    sudah_ada = {p.kode for p in handler.baca_semua_produk()}
    for kode, nama, harga, stok, kat in calon:
        if kode in sudah_ada:
            continue
        try:
            handler.tambah_produk(Produk(kode, nama, harga, stok, kategori=kat))
        except DataError as e:
            print("Produk dilewati:", e)

    olah = OlahInventaris(handler.baca_semua_produk())
    teks = olah.laporan_teks(batas=5)
    handler.tulis_laporan("laporan_akhir.txt", teks)
    print(teks)
    print("Selesai. Laporan ditulis ke laporan_akhir.txt")


if __name__ == "__main__":
    main()
