#fileio.py - semua operasi file (mode x, a, r, w)
from inventaris_pkg.processing import Produk
from inventaris_pkg.validasi import DataError


class FileHandler:
    def __init__(self, nama_file="data_toko.csv"):
        self.nama_file = nama_file

    def inisialisasi_file(self):
        # mode x: buat file pertama kali, tidak menimpa file lama
        try:
            with open(self.nama_file, "x", encoding="utf-8") as f:
                f.write("kode;nama;harga;stok;kategori\n")
            return True
        except FileExistsError:
            return False

    def tambah_produk(self, produk):
        # mode a: tambah di akhir file tanpa menghapus data lama
        d = produk.to_dict()
        with open(self.nama_file, "a", encoding="utf-8") as f:
            f.write(f"{d['kode']};{d['nama']};{d['harga']};{d['stok']};{d['kategori']}\n")

    def baca_semua_produk(self):
        # mode r: baca baris demi baris, baris rusak dilewati
        hasil = []
        try:
            with open(self.nama_file, "r", encoding="utf-8") as f:
                for nomor, baris in enumerate(f, start=1):
                    if nomor == 1 or not baris.strip():
                        continue          # lewati header dan baris kosong
                    kolom = baris.strip().split(";")
                    try:
                        if len(kolom) != 5:
                            raise ValueError("jumlah kolom tidak sesuai")
                        kode, nama, harga, stok, kategori = kolom
                        hasil.append(Produk(kode, nama, float(harga), int(stok),
                                            kategori=kategori))
                    except (ValueError, DataError, AssertionError) as e:
                        print(f"Baris {nomor} dilewati: {e}")
        except FileNotFoundError:
            print(f"Error: file '{self.nama_file}' belum ada.")
        return hasil

    def tulis_laporan(self, nama_laporan, teks):
        # mode w: laporan selalu ditulis baru
        with open(nama_laporan, "w", encoding="utf-8") as f:
            f.write("=== LAPORAN INVENTARIS TOKO ===\n")
            f.write(teks)
